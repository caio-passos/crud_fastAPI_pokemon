from sqlalchemy.orm import Session
from . import models, schemas


def get_pokemonDB(db: Session, ID: int):
    return db.query(models.pokemonData).filter(models.pokemonData.id == ID).first()


def get_allpokemonsDB(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.pokemonData).offset(skip).limit(limit).all()


def add_pokemon(db: Session, pokemon: schemas.pokemon):
    db_pokemon = models.pokemonData(
        Title=models.pokemonData.Title,
        Type=models.pokemonData.Type,
        Total=models.pokemonData.Total,
        HP=models.pokemonData.HP,
        Attack=models.pokemonData.Attack,
        Defense=models.pokemonData.Defense,
        SpAtk=models.pokemonData.SpAtk,
        SpDef=models.pokemonData.SpDef,
        Speed=models.pokemonData.Speed
    )

    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon
