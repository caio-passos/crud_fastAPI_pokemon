from typing import Optional

from pydantic import BaseModel


class pokemon(BaseModel):
    ID: int
    pokemon_name: str
    HP: int
    Attack: int
    Defense: int
    sp_atk: int
    sp_def: int
    speed: int


class pokemonsUpdate(pokemon):
    pokemon_name: Optional[str]
    HP: Optional[int]
    Attack: Optional[int]
    Defense: Optional[int]
    sp_atk: Optional[int]
    sp_def: Optional[int]
    speed: Optional[int]


class pokemonsRemove(pokemon):
    ID: int
    pass
