from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import uuid

app = FastAPI(title="Student Remark NLP Analyzer")

# Load NLP models at startup (first run will download models)
sentiment_analyzer = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

tag_classifier = pipeline(
    task="zero-shot-classification",
    model="facebook/bart-large-mnli"
)

STUDENT_TAGS = [
    "High Performer",
    "Consistent & Reliable",
    "Needs Academic Support",
    "Engagement / Behavioral Concern",
    "At Risk"
]


class RemarkInput(BaseModel):
    teacher_id: str
    student_id: str
    remark: str


class AnalysisOutput(BaseModel):
    record_id: str
    sentiment: str
    sentiment_score: float
    predicted_tag: str
    confidence: float


def classify_tag(text: str):
    result = tag_classifier(
        text,
        candidate_labels=STUDENT_TAGS,
        multi_label=False
    )
    return result["labels"][0], float(result["scores"][0])


@app.post("/analyze", response_model=AnalysisOutput)
def analyze_remark(data: RemarkInput):
    sentiment_result = sentiment_analyzer(data.remark)[0]
    tag, confidence = classify_tag(data.remark)

    return AnalysisOutput(
        record_id=str(uuid.uuid4()),
        sentiment=sentiment_result["label"],
        sentiment_score=float(sentiment_result["score"]),
        predicted_tag=tag,
        confidence=confidence
    )
