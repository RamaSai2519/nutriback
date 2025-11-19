from bson import ObjectId
from dataclasses import asdict
from models.common import Common
from db.users import get_user_collection
from models.constants import OutputStatus
from db.prefs import get_prefs_collection, get_groceries_collection
from models.interfaces import UpsertPreferencesInput as Input, Output, Ingredient


class Compute:
    def __init__(self, input: Input) -> None:
        self.input = input
        self.user_id = ObjectId(self.input.user_id)
        self.users_collection = get_user_collection()
        self.prefs_collection = get_prefs_collection()
        self.groceries_collection = get_groceries_collection()

    def _get_user(self) -> dict:
        return self.users_collection.find_one({"_id": self.user_id})

    def _merge_ingredients(self, existing: list[dict], new: list[Ingredient]) -> list[dict]:

        ingredient_map = {ing['name']: ing for ing in existing}

        for new_ing in new:
            normalized_name = new_ing.name.lower()
            new_ing_dict = asdict(new_ing)
            new_ing_dict['name'] = normalized_name

            if normalized_name in ingredient_map:
                ingredient_map[normalized_name]['ran_out'] = new_ing.ran_out
            else:
                ingredient_map[normalized_name] = new_ing_dict

        return list(ingredient_map.values())

    def _upsert_preferences(self) -> dict:
        if not self.input.preferences:
            return None

        prefs_data = asdict(self.input.preferences)
        prefs_data['user_id'] = self.user_id
        self.prefs_collection.update_one(
            {'user_id': self.user_id},
            {'$set': prefs_data},
            upsert=True
        )
        return prefs_data

    def _upsert_groceries(self) -> dict:
        if not self.input.ingredients and not self.input.ingredients_to_exclude:
            return None

        existing_groceries = self.groceries_collection.find_one(
            {'user_id': self.user_id})

        if existing_groceries:
            ingredients = self._merge_ingredients(
                existing_groceries.get('ingredients', []),
                self.input.ingredients
            ) if self.input.ingredients else existing_groceries.get('ingredients', [])

            exclusions = list(set(existing_groceries.get('ingredients_to_exclude', [])) | set(
                self.input.ingredients_to_exclude)) if self.input.ingredients_to_exclude else existing_groceries.get('ingredients_to_exclude', [])
        else:
            ingredients = [
                {**asdict(ing), 'name': ing.name.lower()}
                for ing in self.input.ingredients
            ] if self.input.ingredients else []
            exclusions = list(
                self.input.ingredients_to_exclude) if self.input.ingredients_to_exclude else []

        self.groceries_collection.update_one(
            {'user_id': self.user_id},
            {'$set': {
                'ingredients': ingredients,
                'ingredients_to_exclude': exclusions
            }},
            upsert=True
        )
        return self.groceries_collection.find_one({'user_id': self.user_id})

    def compute(self) -> Output:
        if not self._get_user():
            return Output(
                msg="User not found",
                status=OutputStatus.FAILURE
            )

        preferences = self._upsert_preferences()
        groceries = self._upsert_groceries()

        return Output(
            data=Common.jsonify(asdict(Input(
                user_id=self.input.user_id,
                preferences=preferences,
                ingredients=groceries.get(
                    'ingredients') if groceries else None,
                ingredients_to_exclude=groceries.get(
                    'ingredients_to_exclude') if groceries else None
            ))),
            msg="Preferences upserted successfully",
        )
