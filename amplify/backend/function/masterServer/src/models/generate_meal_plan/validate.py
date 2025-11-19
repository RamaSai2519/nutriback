from models.interfaces import MealPreferences as Input
from dataclasses import fields


class Validator:
    def __init__(self, input: Input) -> None:
        self.input = input

    def validate(self) -> tuple:
        input_fields = [f.name for f in fields(Input)]
        for field in input_fields:
            if not hasattr(self.input, field):
                return False, f"Missing value: {field}"

        return True, ""
