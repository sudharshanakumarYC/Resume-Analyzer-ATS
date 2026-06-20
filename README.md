# Resume Analyzer using NLP and Sentence-BERT

An AI-powered Resume Analyzer built using Flask, NLP, and Sentence-BERT that automates resume screening, candidate ranking, and selection based on recruiter requirements.

---

## Features

✅ Upload multiple PDF resumes simultaneously

✅ Extract text from resumes using PDFPlumber

✅ Minimum CGPA filtering

✅ Internship requirement filtering

✅ Semantic resume matching using Sentence-BERT

✅ Keyword-based bonus scoring

✅ Certification-based bonus scoring

✅ Project relevance bonus scoring

✅ Candidate ranking and sorting

✅ Top-N candidate selection

---

## Problem Statement

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing each resume is time-consuming and inefficient.

This project automates the screening process by combining Natural Language Processing (NLP), semantic similarity, and rule-based filtering to identify the most suitable candidates.

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

## System Workflow

```text
Upload Resume
      ↓
PDF Text Extraction
      ↓
CGPA Filter
      ↓
Internship Filter
      ↓
Sentence-BERT Matching
      ↓
Keyword Bonus
      ↓
Certificate Bonus
      ↓
Project Relevance Bonus
      ↓
Final Score Calculation
      ↓
Resume Ranking
      ↓
Top N Candidate Selection
```

---

## Scoring Mechanism

### Base Score

The base score is calculated using Sentence-BERT semantic similarity between recruiter requirements and resume content.

### Additional Scores

#### Keyword Bonus

Additional points are awarded when recruiter-specified keywords are found in the resume.

#### Certification Bonus

Additional points are awarded for matching certifications.

#### Project Bonus

Additional points are awarded when the candidate's profile strongly aligns with the required skills and project requirements.

### Final Score

```text
Final Score =
BERT Similarity Score
+ Keyword Bonus
+ Certification Bonus
+ Project Bonus
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/sudharshanakumarYC/Resume-Analyzer.git
```

### Navigate to Project Folder

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
8. Enter Top-N results.
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
├── .gitignore
│
├── templates/
│   ├── home.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── uploads/
│
├── screenshots/
│   ├── home_page.png
│   ├── upload_page.png
│   └── results_page.png
│
└── README.md
```

---

## Future Enhancements

* Support for DOCX resumes
* Advanced skill extraction
* Named Entity Recognition (NER)
* Resume summarization using LLMs
* Recruiter dashboard
* Cloud deployment
* Candidate recommendation system
* Email notification integration

---

## Results

The system successfully:

* Extracts text from PDF resumes
* Filters candidates based on recruiter-defined criteria
* Calculates semantic similarity using Sentence-BERT
* Scores candidates using multiple evaluation parameters
* Ranks resumes according to relevance
* Returns Top-N matching candidates

---

## Author

### Sudharshan A Kumar

B.Tech Artificial Intelligence & Data Science

VSB College of Engineering

GitHub: https://github.com/sudharshanakumarYC

---

⭐ If you found this project useful, consider giving it a star.
