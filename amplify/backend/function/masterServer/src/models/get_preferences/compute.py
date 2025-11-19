from bson import ObjectId
from dataclasses import asdict
from models.common import Common
from models.constants import OutputStatus
from db.prefs import get_prefs_collection, get_groceries_collection
from models.interfaces import GetPreferencesInput as Input, Output


class Compute:
    def __init__(self, input: Input) -> None:
        self.input = input
        self.user_id = ObjectId(self.input.user_id)
        self.prefs_collection = get_prefs_collection()
        self.groceries_collection = get_groceries_collection()

    def compute(self) -> Output:
        query = {'user_id': self.user_id}
        proj = {'_id': 0, 'user_id': 0}
        prefs = self.prefs_collection.find_one(query, proj)
        groceries = self.groceries_collection.find_one(query, proj)

        return Output(
            data={
                'preferences': prefs,
                'groceries': groceries
            },
            msg="Preferences fetched successfully",
        )
