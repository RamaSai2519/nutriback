from openai import OpenAI
from configs import CONFIG as config


class LLM_Client:
    def __init__(self):
        self.key = config.OSS_API_KEY
        self.base_url = config.OSS_BASE_URL
        self.client = self._create_llm_client()

    def _create_llm_client(self) -> OpenAI:
        return OpenAI(
            api_key=self.key,
            base_url=self.base_url
        )
