
from pydantic import BaseModel

# Define un modelo Pydantic para validar los datos del invitado

class Guest(BaseModel):
    name: str
    state: str
    phone: str
    amount_guests:int
    amount_confirm: int

class GuestGet(BaseModel):
    id: int
    name: str
    state: str
    phone: str
    amount_guests:int
    amount_confirm: int