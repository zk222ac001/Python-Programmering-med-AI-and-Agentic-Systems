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


def generate_response(messages: ResponseInputParam) -> str:
    """Send messages to OpenAI and return the response text."""

    try:
        response = client.responses.create(model=MODEL_NAME, input=messages)

        return response.output_text

    except OpenAIError as error:
        return f"OpenAI API Error: {error}"


messages: ResponseInputParam = [
    {"role": "system", "content": "You are a helpful Python tutor."},
    {"role": "user", "content": "Explain list comprehensions."},
]

response = generate_response(messages)
print(response)
