from flask import Flask, render_template, request
import pdfplumber
import os
import re

os.makedirs("uploads",exist_ok=True)

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text

def extract_cgpa(text):
    match=re.search(
        r"CGPA\s*[:=-]?\s*(\d+\.\d+)",
        text,
        re.IGNORECASE
    )
    if match:
        return float(match.group(1))
    return None

def has_internship(text):
    pattern=r"\b(intern|internship|trainee|apprentice)\b"
    match=re.search(
        pattern,
        text,
        re.IGNORECASE
    )
    return match is not None

@app.route("/")
def home():

    return render_template("home.html")

@app.route("/analyze",methods=["POST"])
def analyze():
    skills=request.form["skills"]
    role=request.form["role"]
    cgpa=request.form["cgpa"]
    certifications=request.form["certifications"]
    keywords=request.form["keywords"]
    internship=request.form["internship"]
    projects=request.form["projects"]
    top_n=int(request.form["top_n"])

    files=request.files.getlist("resumes")

    results=[]

    requirement_text=f"""
    Skills:{skills}
    Role:{role}
    Certifications:{certifications}
    Keywords:{keywords}
    """
    requirement_embedding=model.encode(requirement_text)

    for file in files:
        save_path=(f"uploads/{file.filename}")
        file.save(save_path)

        resume_text=extract_text(save_path)
        resume_cgpa=extract_cgpa(resume_text)

        if cgpa != "":

            if resume_cgpa is None:
                continue

            if resume_cgpa < float(cgpa):
                continue

        if internship=="Yes":
            if not has_internship(resume_text):
                continue

        resume_embedding=model.encode(resume_text)

        bert_score=cosine_similarity(
            [requirement_embedding],
            [resume_embedding]
        )[0][0]*100

        project_bonus=0
        if projects=="Yes":
            skills_embedding=model.encode(skills)

            project_similarity=cosine_similarity(
                [skills_embedding],
                [resume_embedding]
            )[0][0]

            if project_similarity>0.8:
                project_bonus=15
            elif project_similarity>0.6:
                project_bonus=10
            elif project_similarity>0.4:
                project_bonus=5

        keyword_score=0
        for keyword in keywords.split(","):
            keyword=keyword.strip()
            if keyword=="":
                continue
            if keyword.lower() in resume_text.lower():
                keyword_score+=3

        certificate_score=0
        for cert in certifications.split(","):
            cert=cert.strip()
            if cert=="":
                continue
            if cert.lower() in resume_text.lower():
                certificate_score+=3
                
        final_score=(bert_score+keyword_score+certificate_score+project_bonus)

        results.append(
            (
            file.filename,
            round(final_score,2)
            )
        )
        os.remove(save_path)

    results.sort(
        key=lambda x:x[1],
        reverse=True
    )

    result=results[:top_n]

    return render_template(
        "result.html",
        results=result
    )
        
if __name__ == "__main__":
    app.run(debug=True)