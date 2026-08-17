"""
OpenAI Terminal Chatbot
Author: Zuhair

Requirements:
pip install openai python-dotenv
"""

# Import dotenv so the script can read OPENAI_API_KEY from a .env file.
from dotenv import load_dotenv

# Import the OpenAI client and base API error type.
from openai import OpenAI, OpenAIError

# Import os so environment variables can be read.
import os

# Import time so the script can measure response duration.
import time


# Model configuration
MODEL_NAME = "gpt-4o-mini"


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


# Create and return an OpenAI client.
def create_client() -> OpenAI:
    # Load environment variables from .env file
    load_dotenv()

    # Read API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Validate API key
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Please add it to your .env file.")

    # Create OpenAI client
    return OpenAI(api_key=api_key)


# Send prompt to OpenAI and return response.
def generate_response(client: OpenAI, prompt: str) -> str:

    # Send the prompt to OpenAI and return the answer.
    try:
        # Call the Responses API with the configured model and user prompt.
        response = client.responses.create(model=MODEL_NAME, input=prompt)

        # Return the text portion of the response.
        return response.output_text

    # Handle OpenAI-specific API errors.
    except OpenAIError as error:
        return format_openai_error(error)

    # Handle unexpected local errors without crashing the chatbot.
    except Exception as error:
        return f"Unexpected Error: {error}"


#  Main chatbot loop.
def main():

    # Try to create the API client before starting the chat loop.
    try:
        client = create_client()

    # Stop early if the .env file is missing the API key.
    except ValueError as error:
        print(f"\nConfiguration Error: {error}")
        return

    # Stop early for any other startup problem.
    except Exception as error:
        print(f"\nStartup Error: {error}")
        return

    # Print a simple startup banner.
    print("=" * 50)
    print("[BOT] OpenAI Chatbot Started")
    print(f"Model: {MODEL_NAME}")
    print("Type 'exit' or 'quit' to stop")
    print("=" * 50)

    while True:
        # Keep each chat turn isolated so one bad input does not stop the program.
        try:
            # Get user input
            prompt = input("\nPlease enter a message: ").strip()

            # Validate empty input
            if not prompt:
                print("Please enter a message.")
                continue

            # Exit condition
            if prompt.lower() in ["exit", "quit"]:
                print("\nGoodbye!")
                break

            # Show thinking message
            print("\nAssistant is thinking...")

            # Start timer
            start_time = time.time()

            # Generate response
            response = generate_response(client, prompt)

            # Calculate processing time
            processing_time = time.time() - start_time

            # Display response
            print("\nAssistant:")
            print(response)

            # Display processing time
            print(f"\nResponse generated in {processing_time:.2f} seconds")

        # Allow the user to stop the program with Ctrl+C.
        except KeyboardInterrupt:
            print("\n\nChat interrupted. Goodbye!")
            break

        # Show any unexpected loop error and continue.
        except Exception as error:
            print(f"\nUnexpected Error: {error}")


# Entry point
if __name__ == "__main__":
    main()
