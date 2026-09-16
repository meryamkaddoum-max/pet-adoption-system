from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models, schemas

router = APIRouter(prefix="/adopters", tags=["Adopters"])


# GET ALL
@router.get("/", response_model=list[schemas.Adopter])
def get_adopters(db: Session = Depends(get_db)):
    return db.query(models.Adopter).all()


# CREATE
@router.post("/", response_model=schemas.Adopter)
def create_adopter(adopter: schemas.AdopterCreate, db: Session = Depends(get_db)):
    db_adopter = models.Adopter(**adopter.model_dump())

    db.add(db_adopter)
    db.commit()
    db.refresh(db_adopter)

    return db_adopter


# DELETE
@router.delete("/{adopter_id}")
def delete_adopter(adopter_id: int, db: Session = Depends(get_db)):
    adopter = db.query(models.Adopter).get(adopter_id)
    db.delete(adopter)
    db.commit()
    return {"message": "deleted"}