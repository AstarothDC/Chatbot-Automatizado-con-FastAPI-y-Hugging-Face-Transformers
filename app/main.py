from fastapi import FastAPI
from pydantic import BaseModel
from .chat import get_chat_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
def chat_endpoint(request: ChatRequest):
    reply = get_chat_response(request.message)
    return {"response": reply}
