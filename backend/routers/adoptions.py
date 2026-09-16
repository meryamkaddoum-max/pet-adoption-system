from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import models, schemas

router = APIRouter(prefix="/adoptions", tags=["Adoptions"])


# GET
@router.get("/", response_model=list[schemas.Adoption])
def get_adoptions(db: Session = Depends(get_db)):
    return db.query(models.Adoption).all()


# CREATE
@router.post("/", response_model=schemas.Adoption)
def create_adoption(adoption: schemas.AdoptionCreate, db: Session = Depends(get_db)):

    db_adoption = models.Adoption(**adoption.model_dump())

    db.add(db_adoption)
    db.commit()
    db.refresh(db_adoption)

    return db_adoption


# DELETE
@router.delete("/{adoption_id}")
def delete_adoption(adoption_id: int, db: Session = Depends(get_db)):
    adoption = db.query(models.Adoption).get(adoption_id)
    db.delete(adoption)
    db.commit()
    return {"message": "deleted"}