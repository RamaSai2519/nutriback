from db import Database
from pymongo.collection import Collection


def get_prefs_collection() -> Collection:
    client = Database().client

    db = client['nutridb']
    prefs_collection = db["preferences"]
    return prefs_collection


def get_groceries_collection() -> Collection:
    client = Database().client

    db = client['nutridb']
    groceries_collection = db["groceries"]
    return groceries_collection
