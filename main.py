from fastapi import FastAPI
from pydantic import BaseModel
import cheesechat.chat


class message(BaseModel):
    text: str


app = FastAPI()
body = {"name": "cheese", "message": [{"content": "你好", "tool": "chat", "message_type": 0}], "conversationId": "612"}


@app.get("/")
async def root():
    return {"message": "welcome"}


@app.post("/chat")
async def chat(text: message):
    body["message"][0]["content"] = text.text
    ret = cheesechat.chat.send_text(body)
    return {"ret": ret}





