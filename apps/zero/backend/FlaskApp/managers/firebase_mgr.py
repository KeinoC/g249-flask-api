from flask import Flask, request
import os
# Don't forget to initialize the environment before installation
# If it's a new app, run `pip3 install firebase-admin`
import firebase_admin
from firebase_admin import credentials, firestore

from utils.singleton_exception import SingletonException




class FirebaseManager():
  init= False
  db = None
  auth = None
  def __init__(self) -> None:
    if (self.init):
      raise SingletonException
    else:
      self.init =True
      cred = credentials.Certificate("serviceAccountKey.json")
      firebase_admin.initialize_app(cred)
      self.db = firestore.client()

  def remove_collection(self, collection):
    collection_ref = self.db.collection(collection)
    docs = collection_ref.get()
    for doc in docs:
        doc.reference.delete()

        



def connect_to_firebase_https(database_url,storage_bucket):
    firebase_admin.initialize_app(
        options={
            "databaseURL": database_url,
            "storageBucket":storage_bucket
        }
    )