from http import HTTPStatus
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from .database import PokemonDBSession, engine, Base
from . import crud, models, schemas
from .models import pokemonData
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = PokemonDBSession()
    try:
        yield db
    finally:
        db.close()
        # dependency


@app.get("/pokemonslist")
def Pokemon(db: PokemonDBSession = Depends(get_db)):
    pokemons = crud.get_allpokemonsDB(db)
    if not pokemons:
        raise HTTPException(status_code=404, detail="DB is empty")
    return dict(pokemons=pokemons)


@app.post("/addPokemon/", response_model=schemas.pokemon)
def addPokemon(pokemon: schemas.pokemon, db: PokemonDBSession = Depends(get_db)):
    return crud.add_pokemon(db=db, pokemon=pokemon)
