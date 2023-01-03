import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents, initialize firebase app
cred = credentials.Certificate('C:/Users/andre/gpugap/flask-server/firebase-sdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://gpugap-56186-default-rtdb.firebaseio.com/'
})

# create gpu spec database in firebase for each manufacturer
ref = db.reference('/')
amd_db_ref = ref.child('amd_db')
nvidia_db_ref = ref.child('nvidia_db')
intel_db_ref = ref.child('intel_db')