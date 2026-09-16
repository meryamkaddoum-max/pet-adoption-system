from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base



class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    species = Column(String)
    breed = Column(String)     # NEU
    gender = Column(String)    # NEU
    age = Column(Integer)
    status = Column(String)


class Adopter(Base):
    __tablename__ = "adopters"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)


class Adoption(Base):
    __tablename__ = "adoptions"

    id = Column(Integer, primary_key=True, index=True)
    adoption_date = Column(Date)
    status = Column(String)

    pet_id = Column(Integer, ForeignKey("pets.id"))
    adopter_id = Column(Integer, ForeignKey("adopters.id"))