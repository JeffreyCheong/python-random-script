import pyrebase
import pymongo
import logging
from decouple import config

pyrebase_config = {
    "apiKey": config('RD_APIKEY'),
    'databaseURL' : config('RD_DATABASE_URL'),
    "authDomain": config('RD_AUTH_DOMAIN'),
    "projectId": config('RD_PROJECT_ID'),
    "storageBucket": config('RD_STORAGE_BUCKET'),
    "messagingSenderId": config('RD_MESSAGING_SENDER_ID'),
    "appId": config('RD_APP_ID'),
    "measurementId": config('RD_MEASUREMENT_ID')
}

client = pymongo.MongoClient("localhost", 27017)
db = client.conversation
collection = db.data
def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    conversation = {
        'conversation_id': message["path"],
        'data': message["data"]
    }

    collection.insert_one(conversation)

if __name__ == '__main__':
    app = pyrebase.initialize_app(pyrebase_config)
    db = app.database()

    my_stream = db.child("conversations").stream(stream_handler)