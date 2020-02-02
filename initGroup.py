import pymongo
import os
from datetime import datetime, timedelta

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