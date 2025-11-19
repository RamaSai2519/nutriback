import json
import dataclasses
from flask import request
from flask_restful import Resource
from models.user_login.main import UserLogin
from models.upsert_user.main import UpsertUser
from models.get_preferences.main import GetPreferences
from models.upsert_preferences.main import UpsesrtPreferences
from models.interfaces import User, LoginInput, MealPreferences, UpsertPreferencesInput, Ingredient, GetPreferencesInput


class UserService(Resource):

    def post(self) -> dict:
        input = json.loads(request.get_data())
        input = User(**input)
        output = UpsertUser(input).process()
        output = dataclasses.asdict(output)

        return output


class UserLoginService(Resource):

    def post(self) -> dict:
        input = json.loads(request.get_data())
        input = LoginInput(**input)
        output = UserLogin(input).process()
        output = dataclasses.asdict(output)

        return output


class UpsertPreferencesService(Resource):

    def format_input(self, input_data: dict) -> UpsertPreferencesInput:
        meal_preferences = input_data.get('preferences', {})
        input_data['preferences'] = MealPreferences(**meal_preferences)
        ingredients = input_data.get('ingredients', [])
        input_data['ingredients'] = [Ingredient(
            **ingredient) for ingredient in ingredients]
        return UpsertPreferencesInput(**input_data)

    def post(self) -> dict:
        input = json.loads(request.get_data())
        input = self.format_input(input)
        output = UpsesrtPreferences(input).process()
        output = dataclasses.asdict(output)

        return output

    def get(self) -> dict:
        input = request.args
        input = GetPreferencesInput(**input)
        output = GetPreferences(input).process()
        output = dataclasses.asdict(output)

        return output
