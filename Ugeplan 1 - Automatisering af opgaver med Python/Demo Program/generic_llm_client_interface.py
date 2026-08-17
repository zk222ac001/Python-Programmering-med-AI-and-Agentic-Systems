"""Shared interface classes for calling different LLM providers."""

# Import tools for defining an abstract base class.
from abc import ABC, abstractmethod


# Define the common interface that every LLM client must implement.
class LLMClient(ABC):
    # Force subclasses to provide their own generate method.
    @abstractmethod
    def generate(self, prompt: str) -> str:
        # Abstract methods do not contain working logic in the base class.
        pass


# Wrap a Google Gemini client behind the shared LLMClient interface.
class GeminiClient(LLMClient):
    # Store the provider client and model name for later use.
    def __init__(self, client, model="gemini-2.5-flash"):
        self.client = client
        self.model = model

    # Send a prompt to Gemini and return text.
    def generate(self, prompt: str) -> str:
        # Convert provider errors into readable strings for demo code.
        try:
            # Call Gemini's content-generation endpoint.
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            # Return Gemini's generated text.
            return response.text
        except Exception as e:
            # Keep the script running and show the error to the learner.
            return f"Gemini Error: {e}"


# Wrap an OpenAI client behind the shared LLMClient interface.
class OpenAIClient(LLMClient):
    # Store the provider client and model name for later use.
    def __init__(self, client, model="gpt-4.1-mini"):
        self.client = client
        self.model = model

    # Send a prompt to OpenAI and return text.
    def generate(self, prompt: str) -> str:
        # Convert provider errors into readable strings for demo code.
        try:
            # Call OpenAI's Responses API with the selected model.
            response = self.client.responses.create(
                model=self.model,
                input=prompt
            )
            # Return the combined text output.
            return response.output_text
        except Exception as e:
            # Read the provider error code when one is available.
            error_code = getattr(e, "code", None)

            # Show a friendly message for the most common classroom API issue.
            if error_code in {"credit_balance_exhausted", "insufficient_quota"}:
                return (
                    "OpenAI Error: your account quota or credits are exhausted. "
                    "Check your OpenAI billing/usage, then run the script again."
                )

            # Return any other OpenAI error without stopping the whole script.
            return f"OpenAI Error: {e}"


# Wrap an Anthropic Claude client behind the shared LLMClient interface.
class ClaudeClient(LLMClient):
    # Store the provider client and model name for later use.
    def __init__(self, client, model="claude-sonnet-4-5"):
        self.client = client
        self.model = model

    # Send a prompt to Claude and return text.
    def generate(self, prompt: str) -> str:
        # Convert provider errors into readable strings for demo code.
        try:
            # Call Claude's messages API.
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            # Return the first text block in Claude's response.
            return response.content[0].text
        except Exception as e:
            # Keep the script running and show the error to the learner.
            return f"Claude Error: {e}"


# Use any LLMClient implementation through one small service class.
class AIService:
    # Store the selected LLM client.
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    # Ask the selected client to generate an answer.
    def ask(self, prompt: str) -> str:
        return self.llm_client.generate(prompt)

    # Print a prompt and its response in a consistent format.
    def print_response(self, prompt: str):
        # Label the prompt section.
        print("\nPROMPT:")

        # Print the exact prompt being sent.
        print(prompt)

        # Label the response section.
        print("\nRESPONSE:")

        # Generate and print the answer.
        print(self.ask(prompt))

        # Separate one example from the next.
        print("-" * 80)
