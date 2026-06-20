from abc import ABC, abstractmethod

# Base Class 
class LLMClient(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class GeminiClient(LLMClient):
    def __init__(self, client, model="gemini-2.5-flash"):
        self.client = client
        self.model = model

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Gemini Error: {e}"


class OpenAIClient(LLMClient):
    def __init__(self, client, model="gpt-4.1-mini"):
        self.client = client
        self.model = model

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.responses.create(
                model=self.model,
                input=prompt
            )
            return response.output_text
        except Exception as e:
            return f"OpenAI Error: {e}"


class ClaudeClient(LLMClient):
    def __init__(self, client, model="claude-sonnet-4-5"):
        self.client = client
        self.model = model

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Claude Error: {e}"


class AIService:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def ask(self, prompt: str) -> str:
        return self.llm_client.generate(prompt)

    def print_response(self, prompt: str):
        print("\nPROMPT:")
        print(prompt)

        print("\nRESPONSE:")
        print(self.ask(prompt))

        print("-" * 80)