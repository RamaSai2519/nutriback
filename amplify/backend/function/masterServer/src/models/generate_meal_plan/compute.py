from models.interfaces import MealPreferences as Input, Output, MealPlan
from helpers.openai import LLM_Client
from models.common import Common
from bson import ObjectId
import json


class Compute:
    def __init__(self, input: Input) -> None:
        self.input = input
        self.llm_client = LLM_Client().client
        self.user_id = ObjectId(self.input.user_id)

    

    def build_chat(self) -> list:
        chat_messages = [
            {
                "role": "user",
                "content": f"Generate a meal plan based on the following preferences: {json.dumps(self.input.__dict__)}."
            }
        ]
        return chat_messages

    def compute(self) -> Output:
        MealPlan.model_rebuild()
        chat_messages = self.build_chat()
        response = self.llm_client.responses.parse(
            model="meituan/longcat-flash-chat:free",
            input=chat_messages,
            text_format=MealPlan
        )
        generated_plan = response.output_parsed
        print("LLM Response:", generated_plan)

        return Output(
            data=Common.jsonify(generated_plan),
            status="SUCCESS"
        )
