
from pydantic import BaseModel

# Define un modelo Pydantic para validar los datos del invitado

class Guest(BaseModel):
    firstname: str
    lastname: str
    state: str
    phone: str
    amount_guests:int
    amount_confirm: int
    menu: str
    music: str

class GuestGet(BaseModel):
    id: int
    firstname: str
    lastname: str
    state: str
    phone: str
    amount_guests:int
    amount_confirm: int
    menu: str
    music: str