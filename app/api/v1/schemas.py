from pydantic import BaseModel, Field
class PromptIn(BaseModel):
    text: str = Field(..., min_length=1, max_length=4000)
class GenerateOut(BaseModel):
    reply: str
    image_url: str | None = None
    audio_url: str | None = None
