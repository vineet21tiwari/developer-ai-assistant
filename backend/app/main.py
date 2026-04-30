from fastapi import FastAPI
from app.api import auth, documents, chat, quiz, code_assistant

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(documents.router, prefix="/documents")
app.include_router(chat.router, prefix="/chat")
app.include_router(quiz.router, prefix="/quiz")
app.include_router(code_assistant.router, prefix="/code")
