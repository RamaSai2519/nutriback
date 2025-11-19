from models.interfaces import GeneratePlanInput as Input, Output, MealPlan
from helpers.openai import LLM_Client
from configs import CONFIG as config
from models.common import Common
from bson import ObjectId
from pprint import pprint
import requests


class Compute:
    def __init__(self, input: Input) -> None:
        self.input = input
        self.llm_client = LLM_Client().client
        self.user_id = ObjectId(self.input.user_id)

    def _get_prefs(self) -> dict:
        url = f'{config.URL}/prefs'
        params = {"user_id": str(self.user_id)}
        response = requests.get(url, params)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch preferences: {response.text}")
        return response.json().get('data', {})

    def build_chat(self) -> list:
        prefs = self._get_prefs()
        ingredients = prefs.get('groceries', {}).get('ingredients', [])
        ingredients = [ing['name']
                       for ing in ingredients if not ing.get('ran_out', False)]
        prefs['groceries'].update({'ingredients': ingredients})

        chat_messages = [
            {
                "role": "user",
                "content": f"Generate a meal plan based on the following preferences: {prefs}."
            }
        ]
        pprint(chat_messages)
        return chat_messages

    def compute(self) -> Output:
        MealPlan.model_rebuild()
        chat_messages = self.build_chat()
        return Output()
        response = self.llm_client.responses.parse(
            model="meituan/longcat-flash-chat:free",
            input=chat_messages,
            text_format=MealPlan
        )
        generated_plan = response.output_parsed
        print("LLM Response:", generated_plan)

        return Output(
            data=Common.jsonify(generated_plan),
        )
