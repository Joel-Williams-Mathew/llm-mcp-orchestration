from fastapi import FastAPI

from backend.api.chat import router as chat_router


app = FastAPI(
    title="OmniAgent",
    description="LLM + MCP Multi-Agent Orchestration Platform",
    version="0.1.0"
)


app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "name": "OmniAgent",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }