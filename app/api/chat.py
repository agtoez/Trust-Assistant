from fastapi import APIRouter
from app.models.conversation import ChatMessage

router = APIRouter(prefix="/chat", tags=["Chat"])

conversation_history = []

@router.post("/")
def chat_endpoint(msg: ChatMessage):
    conversation_history.append(msg)

    return {
        "reply": "Gracias por tu mensaje. Un asesor te responderá a la brevedad",
        "received": msg
    }