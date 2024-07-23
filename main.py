from http import HTTPStatus
from sqlalchemy.orm import Session
from dividendio.database import PokemonDBSession
from fastapi import FastAPI, Depends
from .database import PokemonDBSession, engine, Base
from dividendio.schemas import pokemonDB, pokemon
from . import crud, models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = PokemonDBSession()
    try:
        yield db
    finally:
        db.close()
        # dependency


"""@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
"""


@app.get("/Pokemonslist/", response_model=list[schemas.pokemon])
def Pokemon(skip: int = 0, limit: int = 100, db: PokemonDBSession = Depends(get_db)):
    pokemon = crud.get_allpokemonsDB(db, skip=skip, limit=limit)
    return pokemon


@app.post("/addPokemon/", response_model=schemas.pokemon)
def addPokemon(pokemon: schemas.pokemon, db: PokemonDBSession = Depends(get_db)):
    return crud.add_pokemon(db=db, pokemon=pokemon)
