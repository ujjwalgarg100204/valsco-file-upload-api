from fastapi import APIRouter
from pydantic import BaseModel

controller = APIRouter()


class ChatPrompt(BaseModel):
    """
    Represents a chat prompt.

    Attributes:
        prompt (str): The chat prompt.
    """
    prompt: str


@controller.post("/chat")
async def chat_handler(chat: ChatPrompt):
    rev_chat_prompt = chat.prompt.split(" ")[::-1]
    return {
        "res": rev_chat_prompt
    }
