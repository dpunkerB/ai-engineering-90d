
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="AI Engineering API",
    description="My first AI engineering backend",
    version="0.1.0"
)


class TextAnalysisRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=10000,
        description="Text to analyze"
    )


class TextAnalysisResponse(BaseModel):
    character_count: int
    word_count: int
    estimated_reading_minutes: float


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ai-engineering-api"
    }


@app.post("/analyze", response_model=TextAnalysisResponse)
def analyze_text(request: TextAnalysisRequest):

    text = request.text.strip()

    if not text:
        raise HTTPException(
            status_code=422,
            detail="Text cannot contain only whitespace"
        )

    words = text.split()

    return TextAnalysisResponse(
        character_count=len(text),
        word_count=len(words),
        estimated_reading_minutes=round(
            len(words) / 200, 2
        )
    )
