from db import Database
from pymongo.collection import Collection


def get_user_collection() -> Collection:
    # _id: ObjectId
    # name: str
    # email: str or phone: str
    # password: str (hashed)
    # createdDate: datetime

    client = Database().client

    db = client['nutridb']
    users_collection = db["users"]
    return users_collection
