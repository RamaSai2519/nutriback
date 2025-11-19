from db import Database
from pymongo.collection import Collection


def get_prefs_collection() -> Collection:
    # _id: ObjectId
    # user_id: ObjectId (reference to Users collection)
    # days: int
    # goal: str
    # servings: int
    # cook_time: str
    # skill_level: str
    # meal_types: list[str]
    # restrictions: list[str]

    client = Database().client

    db = client['nutridb']
    prefs_collection = db["preferences"]
    return prefs_collection


def get_groceries_collection() -> Collection:
    # _id: ObjectId
    # user_id: ObjectId (reference to Users collection)
    # ingredients: list[dict[str, any]]
    # ingredients_to_exclude: list[str]

    client = Database().client

    db = client['nutridb']
    groceries_collection = db["groceries"]
    return groceries_collection
