from dotenv import load_dotenv
import os
import json
import firebase_admin
from firebase_admin import credentials, auth

load_dotenv(dotenv_path="firebase_credentials.env")

cred_json = os.environ.get("FIREBASE_CREDENTIALS")
if not cred_json:
    raise Exception("FIREBASE_CREDENTIALS not found")

cred_dict = json.loads(cred_json)

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
