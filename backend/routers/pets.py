from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Pet
from backend.schemas import Pet as PetSchema, PetCreate

router = APIRouter(prefix="/pets", tags=["Pets"])

# =========================
# GET ALL PETS
# =========================
@router.get("/", response_model=list[PetSchema])
def get_pets(db: Session = Depends(get_db)):
    return db.query(Pet).all()

# =========================
# CREATE PET
# =========================
@router.post("/", response_model=PetSchema)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    db_pet = Pet(**pet.model_dump())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

# =========================
# DELETE PET
# =========================
@router.delete("/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    db.delete(pet)
    db.commit()
    return {"message": "Pet deleted"}

# =========================
# UPDATE PET
# =========================
@router.put("/{pet_id}", response_model=PetSchema)
def update_pet(pet_id: int, updated_pet: PetCreate, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    for key, value in updated_pet.model_dump().items():
        setattr(pet, key, value)

    db.commit()
    db.refresh(pet)
    return pet