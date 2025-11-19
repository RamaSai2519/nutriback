from db.users import get_user_collection
from models.constants import OutputStatus
from db.prefs import get_prefs_collection, get_groceries_collection
from models.interfaces import UpsertPreferencesInput as Input, Output

# TODO: Implement the compute logic for upserting preferences and groceries
# Validate user existence
# Check if ingredients or exclusions are provided in input
# existing = [lemons, cilantro]
# input = [chicken, lemons]
# updated = [chicken, cilantro, lemons]
# Upsert into preferences and groceries collections


class Compute:
    def __init__(self, input: Input) -> None:
        self.input = input
        self.users_collection = get_user_collection()
        self.prefs_collection = get_prefs_collection()
        self.groceries_collection = get_groceries_collection()

    def compute(self) -> Output:

        return Output(
            data={},
            msg="Preferences upserted successfully",
            status=OutputStatus.SUCCESS
        )


# Users Collection Structure
# _id: ObjectId
# name: str
# email: str or phone: str
# password: str (hashed)
# createdDate: datetime

# Preferences Collection Structure
# _id: ObjectId
# user_id: ObjectId (reference to Users collection)
# days: int
# goal: str
# servings: int
# cook_time: str
# skill_level: str
# meal_types: list[str]
# restrictions: list[str]

# Groceries Collection Structure
# _id: ObjectId
# user_id: ObjectId (reference to Users collection)
# ingredients: list[dict[str, any]]
# ingredients_to_exclude: list[str]
