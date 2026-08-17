"""Minimal OpenAI Responses API demo."""

# Import dotenv so OPENAI_API_KEY can be loaded from .env.
from dotenv import load_dotenv

# Import the OpenAI client and API error classes used by this demo.
from openai import OpenAI, OpenAIError, RateLimitError

# Loads OPENAI_API_KEY from the .env file.
load_dotenv()

# The name of the OpenAI model to use.
# Keep this aligned with a model available on your OpenAI account.
MODEL_NAME = "gpt-4o-mini"


# Run the OpenAI request and print either the answer or a readable error.
def main():
    # Use try/except so API errors do not crash the script with a long traceback.
    try:
        # Creates an API client and reads OPENAI_API_KEY from the environment.
        client = OpenAI()

        # Send one prompt to OpenAI's Responses API.
        response = client.responses.create(
            model=MODEL_NAME,
            # Defines stable application behaviour
            instructions=(
                "You are a patient Python teacher. "
                "Use simple language and executable examples."
            ),
            # Contains the current user request
            input=(
                "Explain Python lists to a beginner. "
                "Include one example and one exercise."
            ),
        )

        # Returns the combined textual result
        print(response.output_text)

    # Handle rate-limit and quota-related API errors.
    except RateLimitError as error:
        # Read the error code when OpenAI provides one.
        error_code = getattr(error, "code", None)

        # Give a helpful message when the account has no remaining quota.
        if error_code in {"credit_balance_exhausted", "insufficient_quota"}:
            print("OpenAI API Error: your account quota or credits are exhausted.")
            print("Check your OpenAI billing/usage, then run the script again.")

        # Show other rate-limit errors without hiding useful details.
        else:
            print(f"OpenAI API Rate Limit Error: {error}")

    # Handle other OpenAI API errors.
    except OpenAIError as error:
        print(f"OpenAI API Error: {error}")


# Execute main only when this file is run directly.
if __name__ == "__main__":
    main()
