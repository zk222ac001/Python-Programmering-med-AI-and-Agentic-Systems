# Python application that sends prompts to OpenAI and 
# receives responses programmatically.
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
from openai.types.responses import ResponseInputParam
import os

load_dotenv()

MODEL_NAME = "gpt-4o-mini"

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

client = OpenAI()


def format_openai_error(error: OpenAIError) -> str:
    error_code = getattr(error, "code", None)
    if error_code in {"credit_balance_exhausted", "insufficient_quota"}:
        return (
            "OpenAI API Error: your account quota or credits are exhausted. "
            "Check your OpenAI billing/usage, then run the script again."
        )
    return f"OpenAI API Error: {error}"


def generate_response(messages: ResponseInputParam) -> str:
    """Send messages to OpenAI and return the response text."""

    try:
        response = client.responses.create(model=MODEL_NAME, input=messages)

        return response.output_text

    except OpenAIError as error:
        return format_openai_error(error)


messages: ResponseInputParam = [
    {"role": "system", "content": "You are a helpful Python tutor."},
    {"role": "user", "content": "Explain list comprehensions."},
]

response = generate_response(messages)
print(response)
