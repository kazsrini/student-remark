# Student Remark NLP Analyzer

A FastAPI-based backend service that performs sentiment analysis and student tagging on free-text teacher remarks using NLP models.

This project is designed as an MVP for educational analytics, helping schools or educators extract structured insights from qualitative feedback.

## Features:

- Accepts teacher remarks via a REST API

- Performs sentiment analysis (positive / negative)

- Classifies students into 5 predefined tags

- Auto-generated API documentation (Swagger UI)

- Fully version-controlled with Git & GitHub

## Student Tags

The system assigns one dominant tag per remark:

1. High Performer

2. Consistent & Reliable

3. Needs Academic Support

4. Engagement / Behavioral Concern

5. At Risk

## Tech Stack

- Python 3.9+

- FastAPI – API framework

- Uvicorn – ASGI server

- HuggingFace Transformers

- PyTorch

- Git & GitHub

## Setup Instructions 

### 1. Clone the repository 

`git clone https://github.com/kazsrini/student-remark.git
cd student-remark` 

### 2. Create and activate virtual environment

`python3 -m venv .venv`

`source .venv/bin/activate`

### 3. Install Dependencies 

`pip install -r requirements.txt`

### 4. Run the Server 

`uvicorn app.main:app --reload`

## Testing the API 

Open your browser and go to 

`http://127.0.0.1:8000/docs`

## Sample request 

{

  "teacher_id": "T001",
  
  "student_id": "S123",
  
  "remark": "Struggles with homework and lacks focus in class."
  
}

## Sample response 

{

  "record_id": "uuid",
  
  "sentiment": "NEGATIVE",
  
  "sentiment_score": 0.98,
  
  "predicted_tag": "Needs Academic Support",
  
  "confidence": 0.72
  
}

## Future Enhancements 

- SQLite / PostgreSQL persistence

- Student-level analytics & trends

- Fine-tuned NLP classifier

- Authentication & role-based access

- Deployment to cloud (Docker / AWS / GCP)


