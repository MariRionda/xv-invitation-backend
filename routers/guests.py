from fastapi import APIRouter, HTTPException
from db import get_database
from typing import List
from models import Guest
from google.cloud import firestore


router = APIRouter()

db = get_database()

# Define la ruta POST para crear un nuevo invitado
@router.post("/")
async def create_guest(guest: Guest):
    try:
        # Obtiene el número máximo actual de los documentos en la colección de invitados
        query = db.collection('guests').order_by('id', direction=firestore.Query.DESCENDING).limit(1)
        docs = query.stream()
        last_id = 0
        for doc in docs:
            last_id = doc.get('id')
            break

        # Suma 1 al número máximo para obtener el nuevo ID
        new_id = last_id + 1

        # Formatea el nuevo ID como una cadena de 3 dígitos con ceros a la izquierda
        id_str = str(new_id)

        # Crea el nuevo documento en Firestore con el ID y los datos del invitado
        doc_ref = db.collection('guests').document(id_str)
        doc_ref.set({
            'id': new_id,
            'name': guest.name,
            'state': guest.state,
            'phone': guest.phone,
            'amount_guests': guest.amount_guests,
            'amount_confirm': guest.amount_confirm
        })
        return {'msg': 'El invitado ha sido creado correctamente'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define la ruta GET para obtener todos los invitados
# Ruta GET para obtener todos los clientes
@router.get("/all")
async def get_guests():
    try:
        guests = []
        # Obtiene todos los documentos de la colección "compras"
        docs = db.collection('guests').get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            guest = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            guests.append(guest)
        return guests
    except Exception as e:
        print(e)
        return {"message":"Ocurrió un error inesperado ","status_code":400}
    
# Define la ruta DELETE para eliminar un invitado por su ID
@router.delete("/{guest_id}")
async def delete_guest(guest_id: str):
    try:
        # Verifica si el invitado existe en Firestore
        doc_ref = db.collection('guests').document(guest_id)
        doc = doc_ref.get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail='El invitado no existe')

        # Elimina el documento del invitado
        doc_ref.delete()
        return {'msg': 'El invitado ha sido eliminado correctamente'}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

