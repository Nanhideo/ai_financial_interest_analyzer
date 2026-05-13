from fastapi import FastAPI
from routes.finance import router

app = FastAPI(
    title="Financial AI API",
    description="A all in one LLM based financial interest analyzer and AI advisor API .",
    version="1.0.0"
)

# Include the finance router with the /finance prefix
app.include_router(router, prefix="/finance")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)