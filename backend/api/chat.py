from fastapi import APIRouter
from pydantic import BaseModel

from backend.llm.provider import generate_response

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = generate_response(request.message)

    return ChatResponse(
        response=response
    )