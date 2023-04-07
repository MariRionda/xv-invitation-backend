from google.cloud import firestore

def get_database():
    db = firestore.Client.from_service_account_json('firebase.json')
    return db