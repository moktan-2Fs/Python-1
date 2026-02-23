from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow the frontend (HTML file) to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# This is the shape of the request coming from the frontend


class Message(BaseModel):
    message: str


@app.post("/chat")
def chat(body: Message):
    # Send the message to Ollama running locally
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1",
            "prompt": body.message,
            "stream": False       # wait for full response, no streaming
        },
        timeout=120              # wait up to 2 minutes for llama3 to respond
    )

    data = response.json()

    # Temporary: print the full response so we can see its structure
    print("Llama response:", data)

    # Send the response text back to the frontend
    return {"response": data["response"]}
