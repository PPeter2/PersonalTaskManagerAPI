from fastapi import FastAPI
from app.database import engine, Base
from app.api.tasks import router as tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI( 
    title="Personal Task Manager API",
    description="A simple task manager API",
    version="1.0.0"
)

app.include_router(tasks_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}