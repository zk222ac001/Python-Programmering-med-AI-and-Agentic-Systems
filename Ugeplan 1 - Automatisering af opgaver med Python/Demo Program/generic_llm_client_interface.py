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
            error_code = getattr(e, "code", None)
            if error_code in {"credit_balance_exhausted", "insufficient_quota"}:
                return (
                    "OpenAI Error: your account quota or credits are exhausted. "
                    "Check your OpenAI billing/usage, then run the script again."
                )
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
