from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title="NeonTrust AI",
    description="Asistente de atención al cliente para cartelería de neón led personalizada",
    version="0.1.0"
)

app.include_router(chat_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
