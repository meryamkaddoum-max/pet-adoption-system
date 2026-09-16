from pydantic import BaseModel
from datetime import date



class PetBase(BaseModel):
    name: str
    species: str
    breed: str
    gender: str
    age: int
    status: str

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int

    class Config:
        from_attributes = True


# ---------- ADOPTER ----------
class AdopterBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str


class AdopterCreate(AdopterBase):
    pass


class Adopter(AdopterBase):
    id: int

    class Config:
        from_attributes = True


# ---------- ADOPTION ----------
class AdoptionBase(BaseModel):
    adoption_date: date   # ❗ wichtig
    status: str
    pet_id: int
    adopter_id: int


class AdoptionCreate(AdoptionBase):
    pass


class Adoption(AdoptionBase):
    id: int

    class Config:
        from_attributes = True