from dotenv import load_dotenv
from openai import OpenAI, OpenAIError, RateLimitError

# Loads OPENAI_API_KEY from the .env file.
load_dotenv()

MODEL_NAME = "gpt-5.6"


def main():
    try:
        # Creates an API client and reads OPENAI_API_KEY from the environment.
        client = OpenAI()

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

    except RateLimitError as error:
        if getattr(error, "code", None) == "credit_balance_exhausted":
            print("OpenAI API Error: your account has no credits remaining.")
            print("Add credits in OpenAI billing, then run the script again.")
        else:
            print(f"OpenAI API Rate Limit Error: {error}")

    except OpenAIError as error:
        print(f"OpenAI API Error: {error}")


if __name__ == "__main__":
    main()
