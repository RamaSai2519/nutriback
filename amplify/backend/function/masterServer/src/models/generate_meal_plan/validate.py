from models.interfaces import GeneratePlanInput as Input
from bson import ObjectId


class Validator:
    def __init__(self, input: Input) -> None:
        self.input = input

    def validate(self) -> tuple:
        if not ObjectId.is_valid(self.input.user_id):
            return False, "Invalid user ID"

        return True, ""
