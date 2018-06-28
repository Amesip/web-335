from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)

print(client)

db = client.web335

user = {

    "first_name": "Anton",

    "last_name": "Weber",

    "email": "aweber@me.com",

    "employee_id": "0000009",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000009"}))

