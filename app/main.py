from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .schemas import SentimentRequest, SentimentResponse


app = FastAPI(title="SentiKampus API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post(
    "/api/v1/predict",
    response_model=SentimentResponse
)
def predict(data: SentimentRequest):
    label = (
        "negative"
        if "lambat" in data.text.lower()
        else "neutral"
    )

    return SentimentResponse(
        label=label,
        score=0.91
    )
