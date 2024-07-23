from sqlalchemy import Column, Integer, String

from .database import Base


class pokemonData(Base):
    __tablename__ = "pokemons"

    ID = Column(Integer, unique=True, primary_key=True)
    Title = Column(String, unique=True, index=True)
    Type = Column(String, index=True)
    Total = Column(Integer, index=True)
    HP = Column(Integer, index=True)
    Attack = Column(Integer, index=True)
    Defense = Column(Integer, index=True)
    SpAtk = Column(Integer, index=True)
    SpDef = Column(Integer, index=True)
    Speed = Column(Integer, index=True)
