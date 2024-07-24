from sqlalchemy.orm import Session
from . import models, schemas
from pydantic import BaseModel


def get_pokemonDB(db: Session, ID: int):
    return db.query(models.pokemonData).filter(models.pokemonData.id == ID).first()


def get_allpokemonsDB(db: Session, skip: int = 0, limit: int = 100):
    all_pokemons = db.query(models.pokemonData).offset(skip).limit(limit).all()
    return all_pokemons


def add_pokemon(db: Session, pokemon: schemas.pokemon):
    db_pokemon = models.pokemonData(**pokemon.dict())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon
