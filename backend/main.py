from fastapi import FastAPI
from backend.routers import pets, adopters, adoptions
from backend.database import engine
from backend.models import Base

app = FastAPI(
    title="Pet Adoption Management System API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(pets.router)
app.include_router(adopters.router)
app.include_router(adoptions.router)

@app.get("/")
def root():
    return {"message": "API läuft"}