# Python application that sends prompts to OpenAI and 
# receives responses programmatically.

# Import dotenv so environment variables can be loaded from .env.
from dotenv import load_dotenv

# Import the OpenAI client and base API error type.
from openai import OpenAI, OpenAIError

# Import the type used for structured Responses API input.
from openai.types.responses import ResponseInputParam

# Import os so the script can read OPENAI_API_KEY from the environment.
import os

# Load values from .env into the process environment.
load_dotenv()

# Store the model name in one place so it can be changed easily.
MODEL_NAME = "gpt-4o-mini"

# Stop immediately if the required API key is missing.
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

# Create the OpenAI client using the environment API key.
client = OpenAI()


# Convert OpenAI exceptions into beginner-friendly messages.
def format_openai_error(error: OpenAIError) -> str:
    # Some OpenAI errors include a machine-readable code.
    error_code = getattr(error, "code", None)

    # Give a clear explanation for exhausted credits or quota.
    if error_code in {"credit_balance_exhausted", "insufficient_quota"}:
        return (
            "OpenAI API Error: your account quota or credits are exhausted. "
            "Check your OpenAI billing/usage, then run the script again."
        )

    # Fall back to the original error text for other API problems.
    return f"OpenAI API Error: {error}"


def generate_response(messages: ResponseInputParam) -> str:
    """Send messages to OpenAI and return the response text."""

    # Send the structured messages to OpenAI.
    try:
        # Call the Responses API with the selected model and messages.
        response = client.responses.create(model=MODEL_NAME, input=messages)

        # Return the combined text output.
        return response.output_text

    # Convert OpenAI errors into readable output.
    except OpenAIError as error:
        return format_openai_error(error)


# Define the system and user messages for one request.
messages: ResponseInputParam = [
    # The system message sets the assistant's behavior.
    {"role": "system", "content": "You are a helpful Python tutor."},

    # The user message asks the actual question.
    {"role": "user", "content": "Explain list comprehensions."},
]

# Generate an answer from OpenAI.
response = generate_response(messages)

# Print the answer or a readable error message.
print(response)
