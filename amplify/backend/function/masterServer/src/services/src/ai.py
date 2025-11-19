import json
import dataclasses
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.interfaces import MealPreferences as Input
from models.generate_meal_plan.main import RecipesGenerator


class MealPlanService(Resource):

    @jwt_required()
    def post(self) -> dict:
        input = json.loads(request.get_data())
        input = Input(**input)
        output = RecipesGenerator(input).process()
        output = dataclasses.asdict(output)

        return output
