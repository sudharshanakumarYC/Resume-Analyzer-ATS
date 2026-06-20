# Resume Analyzer using NLP and Sentence-BERT

## Overview

Resume Analyzer is an AI-powered web application developed using Flask, NLP, and Sentence-BERT. The system helps recruiters and HR professionals automatically analyze and rank resumes based on job requirements. Instead of manually reviewing hundreds of resumes, recruiters can upload multiple resumes at once, specify required skills, certifications, CGPA, internship requirements, and receive a ranked list of candidates.

The project combines traditional filtering techniques with modern Natural Language Processing (NLP) methods to improve candidate selection efficiency.

---

## Features

* Upload and analyze multiple PDF resumes simultaneously
* Automatic text extraction from PDF resumes
* Minimum CGPA filtering
* Internship requirement filtering
* Sentence-BERT based semantic resume matching
* Keyword-based bonus scoring
* Certification-based bonus scoring
* Project relevance bonus scoring
* Candidate ranking based on final score
* Top N candidate selection
* User-friendly web interface

---

## Technologies Used

### Backend

* Python
* Flask

### NLP & Machine Learning

* Sentence-BERT (all-MiniLM-L6-v2)
* Scikit-Learn
* Cosine Similarity

### PDF Processing

* PDFPlumber

### Frontend

* HTML
* CSS

### Other Libraries

* Regex (re)
* OS Module

---

## Problem Statement

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing each resume is time-consuming and inefficient. Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, which may overlook relevant candidates.

This project aims to automate resume screening using NLP techniques, helping recruiters quickly identify the most suitable candidates.

---

## Objectives

* Automate resume screening and ranking
* Reduce manual effort in candidate selection
* Improve candidate matching using semantic similarity
* Filter candidates based on recruiter-defined requirements
* Provide a scalable solution for resume analysis

---

## System Architecture

Recruiter Input
↓
Resume Upload
↓
PDF Text Extraction
↓
CGPA Filtering
↓
Internship Filtering
↓
Sentence-BERT Matching
↓
Keyword Bonus Scoring
↓
Certification Bonus Scoring
↓
Project Relevance Bonus Scoring
↓
Final Score Calculation
↓
Resume Ranking
↓
Top N Candidate Selection

---

## Workflow

### Step 1: Resume Upload

The recruiter uploads one or more PDF resumes through the web interface.

### Step 2: PDF Text Extraction

The system extracts textual content from uploaded PDF files using PDFPlumber.

### Step 3: CGPA Filtering

Candidates whose CGPA is below the recruiter-defined threshold are eliminated.

### Step 4: Internship Filtering

If internship experience is required, resumes without internship-related experience are filtered out.

### Step 5: Semantic Resume Matching

Sentence-BERT converts both job requirements and resume content into vector embeddings.

### Step 6: Similarity Calculation

Cosine Similarity is used to calculate semantic similarity between recruiter requirements and candidate resumes.

### Step 7: Bonus Scoring

Additional points are awarded for:

* Matching keywords
* Relevant certifications
* Relevant projects

### Step 8: Final Ranking

The final score is calculated and candidates are ranked accordingly.

---

## Scoring Mechanism

### Base Score

Sentence-BERT Similarity Score

### Additional Bonus Scores

#### Keyword Bonus

Candidates receive additional points when recruiter-specified keywords are found in the resume.

#### Certification Bonus

Candidates receive bonus points for matching certifications.

#### Project Bonus

Candidates receive additional points when projects demonstrate relevance to the required skills.

### Final Score

Final Score =
BERT Similarity Score +
Keyword Bonus +
Certification Bonus +
Project Bonus

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Resume-Analyzer.git
```

### Navigate to Project Directory

```bash
cd Resume-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Usage

1. Enter required skills.
2. Enter required role.
3. Enter minimum CGPA (optional).
4. Enter required certifications.
5. Enter required keywords.
6. Select internship requirement.
7. Select project prioritization option.
8. Enter Top N results.
9. Upload resumes.
10. Click Analyze.
11. View ranked candidates.

---

## Project Structure

```text
Resume-Analyzer/
│
├── app.py
├── requirements.txt
│
├── uploads/
│
├── templates/
│   ├── home.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── screenshots/
│
└── README.md
```

---

## Future Enhancements

* Support for DOCX resumes
* Advanced project section extraction
* Skill extraction using Named Entity Recognition (NER)
* Resume summarization using Large Language Models (LLMs)
* Recruiter dashboard
* Cloud deployment
* Candidate recommendation system
* Email notification integration

---

## Results

The system successfully:

* Extracts information from PDF resumes
* Filters candidates based on recruiter requirements
* Calculates semantic similarity using Sentence-BERT
* Ranks candidates according to relevance
* Returns Top N matching resumes


## Author

**Sudharshana Kumar**

B.Tech Artificial Intelligence and Data Science

GitHub: https://github.com/sudharshanakumarYC
