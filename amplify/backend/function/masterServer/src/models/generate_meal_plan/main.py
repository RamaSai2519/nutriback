import traceback
from models.constants import OutputStatus
from models.generate_meal_plan.compute import Compute
from models.generate_meal_plan.validate import Validator
from models.interfaces import MealPreferences as Input, Output


class RecipesGenerator:
    def __init__(self, input: Input) -> None:
        self.input = input

    def process(self) -> Output:
        input = self.input
        valid_input, error_message = self._validate(input)

        if not valid_input:
            return Output(
                msg=error_message,
                status=OutputStatus.FAILURE
            )

        try:
            output = self._compute(input)
        except Exception as e:
            print(traceback.format_exc())
            output = Output(
                msg=e, status=OutputStatus.FAILURE
            )

        return output

    def _validate(self, input: Input):
        validation_obj = Validator(input)
        validation_result, error_message = validation_obj.validate()

        return validation_result, error_message

    def _compute(self, input: Input) -> Output:
        computation_obj = Compute(input)
        output = computation_obj.compute()

        return output
