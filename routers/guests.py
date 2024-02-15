from fastapi import APIRouter, HTTPException, Header
from db import get_database
from models import Guest
from google.cloud import firestore


router = APIRouter()

db = get_database()

# Define la ruta POST para crear un nuevo invitado
@router.post("/")
async def create_guest(guest: Guest, collection:str = Header(...)):
    try:
        # Obtiene el número máximo actual de los documentos en la colección de invitados
        query = db.collection(collection).order_by('id', direction=firestore.Query.DESCENDING).limit(1)
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
        doc_ref = db.collection(collection).document(id_str)
        doc_ref.set({
            'id': new_id,
            'firstname': guest.firstname,
            'lastname': guest.lastname,
            'state': guest.state,
            'phone': guest.phone,
            'amount_guests': guest.amount_guests,
            'amount_confirm': guest.amount_confirm,
            'menu': guest.amount_confirm,
            'music': guest.amount_confirm,
        })
        return {'msg': 'El invitado ha sido creado correctamente'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Define la ruta GET para obtener todos los invitados
# Ruta GET para obtener todos los clientes
@router.get("/all")
async def get_guests(collection:str = Header(...)):
    try:
        guests = []
        # Obtiene todos los documentos de la colección "compras"
        docs = db.collection(collection).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            guest = doc.to_dict()
            # Agrega el diccionario a la lista de compras
            guests.append(guest)
        ordered_guests = sorted(guests, key=lambda x: (x['lastname'], x['firstname']))
        return ordered_guests
    except Exception as e:
        print(e)
        return {"message":"Ocurrió un error inesperado ","status_code":400}
    
@router.get("/name/{name}")
async def get_guests_by_name(name: str, collection:str = Header(...)):
    try:
        guests = []
        # Obtiene todos los documentos de la colección "guests"
        docs = db.collection(collection).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            guest = doc.to_dict()
            # Si el firstname y el lastname del invitado coinciden con el name proporcionado,
            # agrega el invitado a la lista de invitados
            if name == guest['lastname'] + ' ' + guest['firstname']:
                guests.append(guest)
        ordered_guests = sorted(guests, key=lambda x: (x['lastname'], x['firstname']))
        return ordered_guests
    except Exception as e:
        print(e)
        return {"message":"Ocurrió un error inesperado ","status_code":400}
    

@router.get("/list")
async def get_guests_not_attend(collection:str = Header(...)):
    try:
        guests = []
        response = {'attend':[], 'not_attend':[], 'not_confirm':[]} 
        # Obtiene solo los documentos de la colección "guests" donde "state" es igual a "No asistiré"
        docs = db.collection(collection).get()
        for doc in docs:
            # Convierte los datos del documento a un diccionario
            guest = doc.to_dict()
            # Agrega el diccionario a la lista de invitados
            guests.append(guest)
        ordered_guests = sorted(guests, key=lambda x: (x['lastname'], x['firstname']))
        for guest in ordered_guests:
            if guest['state']=='Asistiré':
                response['attend'].append(guest)
            if guest['state']=='No asistiré':
                response['not_attend'].append(guest)
            if guest['state']=='No confirmó':
                response['not_confirm'].append(guest)
        return response
    except Exception as e:
        print(e)
        return {"message":"Ocurrió un error inesperado ","status_code":400}
  

# Define la ruta PUT para actualizar las propiedades "state" y "amount_confirm" de un invitado por nombre
@router.put("/")
async def update_guest(guest: Guest, collection:str = Header(...)):
    try:
        # Busque el documento del invitado por su nombre
        query = db.collection(collection).where('firstname', '==', guest.firstname).where('lastname', '==', guest.lastname)
        docs = query.stream()

        # Actualice los campos 'state' y 'amount_confirm' del invitado y guarde el documento
        for doc in docs:
            doc_ref = db.collection(collection).document(doc.id)
            doc_ref.update({
                'state': guest.state,
                'amount_confirm': guest.amount_confirm
            })
            return {'msg': 'Los campos han sido actualizados correctamente'}
        
        # Si no se encuentra el documento del invitado, devuelva un error 404
        raise HTTPException(status_code=404, detail='Invitado no encontrado')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Define la ruta PUT para actualizar la propiedad "music" de un invitado por nombre
@router.put("/music")
async def update_guest(guest: Guest, collection:str = Header(...)):
    try:
        # Busque el documento del invitado por su nombre
        query = db.collection(collection).where('firstname', '==', guest.firstname).where('lastname', '==', guest.lastname)
        docs = query.stream()

        # Actualice el campo 'music' del invitado y guarde el documento
        for doc in docs:
            doc_ref = db.collection(collection).document(doc.id)
            doc_ref.update({
                'music': guest.music
            })
            return {'msg': 'El campo music ha sido actualizado correctamente'}
        
        # Si no se encuentra el documento del invitado, devuelva un error 404
        raise HTTPException(status_code=404, detail='Invitado no encontrado')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Define la ruta PUT para actualizar la propiedad "menu" de un invitado por nombre
@router.put("/menu")
async def update_guest(guest: Guest, collection:str = Header(...)):
    try:
        # Busque el documento del invitado por su nombre
        query = db.collection(collection).where('firstname', '==', guest.firstname).where('lastname', '==', guest.lastname)
        docs = query.stream()

        # Actualice el campo 'menu' del invitado y guarde el documento
        for doc in docs:
            doc_ref = db.collection(collection).document(doc.id)
            doc_ref.update({
                'menu': guest.menu
            })
            return {'msg': 'El campo menu ha sido actualizado correctamente'}
        
        # Si no se encuentra el documento del invitado, devuelva un error 404
        raise HTTPException(status_code=404, detail='Invitado no encontrado')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Define la ruta DELETE para eliminar un invitado por su ID
@router.delete("/{guest_id}")
async def delete_guest(guest_id: str, collection:str = Header(...)):
    try:
        # Verifica si el invitado existe en Firestore
        doc_ref = db.collection(collection).document(guest_id)
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

