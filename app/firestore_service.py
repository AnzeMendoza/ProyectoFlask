import firebase_admin
from firebase_admin import firestore, credentials

project_id = "Backend-Flask-todo"
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users():
    return db.collection("users").get()


def get_todos(user_id):
    return db.collection("users").document(user_id).collection("todos").get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()