import pymongo
import os
from datetime import datetime, timedelta
import requests 

def initGroup(group):
    client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
    db = client["diner-party"]
    people = []

    for person in group.people:
        cook_days = []
        if person.mon.data:
            cook_days.append(0)
        if person.tues.data:
            cook_days.append(1)
        if person.wed.data:
            cook_days.append(2)
        if person.thurs.data:
            cook_days.append(3)
        if person.fri.data:
            cook_days.append(4)
        if person.sat.data:
            cook_days.append(5)
        if person.sun.data:
            cook_days.append(6)

        people.append(db["people"].insert_one(
            {
                "name": person.username.data,
                "number": "+1"+person.phone_number.data,
                "email": person.email.data,
                "cook_days": cook_days,
                "last_question": 0
            }
        ).inserted_id)

    id = db["parties"].insert_one(
        {
            "name": group.groupName.data,
            "people": people,
            "event": None
        }
    ).inserted_id

    for person in people:
        db["people"].update_one(
            {"_id": person},
            {"$set": {"party": id}}
        )

def reset():
    client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
    db = client["diner-party"]

    # Clear collections

    db["parties"].remove({})
    db["people"].remove({})
    db["events"].remove({})

def defaultGroup():
    client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
    db = client["diner-party"]

    people = []

    people.append(db["people"].insert_one(
        {
            "name": "Nick",
            "number": "+12023847411",
            "email": "nick@mittudev.com",
            "cook_days": [0,1,2,3,4,5,6],
            "last_cooked": datetime.now() - timedelta(days=1),
            "percentage": 50,
            "dietary_preferences": ["vegetarian"],
            "last_question": 0
        }
    ).inserted_id)

    people.append(db["people"].insert_one(
        {
            "name": "Anjali",
            "number": "+13019563002",
            "email": "anjmittu@gmail.com",
            "cook_days": [0,1,2,3,4,5,6],
            "last_cooked": datetime.now() - timedelta(days=2),
            "percentage": 50,
            "dietary_preferences": ["vegetarian", "vegan"],
            "last_question": 0
        }
    ).inserted_id)

    people.append(db["people"].insert_one(
        {
            "name": "Ajay",
            "number": "+12405954543",
            "email": "ajaymysore95@gmail.com",
            "cook_days": [],
            "last_cooked": datetime.now() - timedelta(days=1),
            "percentage": 50,
            "dietary_preferences": ["vegetarian"],
            "last_question": 0
        }
    ).inserted_id)

    people.append(db["people"].insert_one(
        {
            "name": "Rohan",
            "number": "+12407082233",
            "email": "rdmittu@gmail.com",
            "cook_days": [],
            "last_cooked": datetime.now() - timedelta(days=1),
            "percentage": 50,
            "dietary_preferences": ["vegetarian", "vegan"],
            "last_question": 0
        }
    ).inserted_id)

    id = db["parties"].insert_one(
        {
            "name": "Dinner Party",
            "people": people,
            "event": None
        }
    ).inserted_id

    for person in people:
        db["people"].update_one(
            {"_id": person},
            {"$set": {"party": id}}
        )

def triggerSMS():
    requests.get(url = os.getenv("TRIGGER_URL"))