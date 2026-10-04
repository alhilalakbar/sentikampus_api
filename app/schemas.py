from pydantic import BaseModel, Field


class SentimentRequest(BaseModel):
    text: str = Field(
        min_length=3,
        max_length=500
    )


class SentimentResponse(BaseModel):
    label: str
    score: float
