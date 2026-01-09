from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "telegram-orquestador-backend"
    }

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    print("Update recibido:", data)
    return {"ok": True}
