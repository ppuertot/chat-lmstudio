"""
FastAPI server for a web chat interface that talks to local AI models loaded in LM Studio.

This is a minimal example – you will need to replace the placeholder `get_local_model_response`
function with code that actually queries your LM Studio model.
"""
import json
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# Mount the static folder to serve index.html and chat.js
app.mount("/static", StaticFiles(directory="static"), name="static")

# Simple in‑memory placeholder for a local model call.
# Replace this with your LM Studio SDK calls.
import os
import requests

# Base URL del servidor de LM Studio. Se puede sobreescribir con la variable de entorno LMSTUDIO_URL.
LMSTUDIO_BASE = os.getenv("LMSTUDIO_URL", "http://localhost:1234")


def get_local_model_response(message: str) -> str:
    """
    Llama al modelo local de LM Studio usando el endpoint `/v1/chat/completions`.
    El modelo por defecto es `openai/gpt-oss‑20b`, pero puedes cambiarlo.
    """
    url = f"{LMSTUDIO_BASE}/v1/chat/completions"
    payload = {
        "model": "openai/gpt-oss-20b",
        "messages": [{"role": "user", "content": message}],
        "max_tokens": 512,
        "temperature": 0.7,
        "stream": False
    }
    try:
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Error llamando a LM Studio: {e}")
    data = resp.json()
    # La respuesta sigue la especificación OpenAI
    return data["choices"][0]["message"]["content"]

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Serve the static index.html directly from the static folder
    return HTMLResponse(open("static/index.html", "r", encoding="utf-8").read())

@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message")
        if not user_message:
            raise HTTPException(status_code=400, detail="Missing 'message' field")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Call the local model
    ai_response = get_local_model_response(user_message)
    return JSONResponse(content={"response": ai_response})

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
