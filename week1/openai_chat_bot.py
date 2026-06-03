# How to generate an OpenAI API key:
# 1. Go to https://platform.openai.com/signup and create an account if you

# Import the function that loads variables from a .env file
from dotenv import load_dotenv

# Import the OpenAI client and OpenAI-specific exceptions
from openai import OpenAI, OpenAIError

# Import Python's built-in os module
# Used to access environment variables
import os

m
# Function responsible for creating the OpenAI client
def create_client() -> OpenAI:
    """Create and return an OpenAI client."""

    # Load environment variables from the .env file
    load_dotenv()

    # Read the API key from the environment
    api_key = os.getenv("OPENAI_API_KEY")

    # If the API key is missing, stop the program
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Please add it to your .env file.")

    # Create and return an OpenAI client
    return OpenAI(api_key=api_key)


# Function that sends a prompt to OpenAI
def generate_response(client: OpenAI, prompt: str) -> str:
    """Send prompt to OpenAI and return the response text."""

    try:
        # Send the user's prompt to the model
        response = client.responses.create(model="gpt-4o-mini", input=prompt)

        # Return only the generated text
        return response.output_text

    # Handle OpenAI-specific errors
    except OpenAIError as error:
        return f"OpenAI API error: {error}"

    # Handle any unexpected errors
    except Exception as error:
        return f"Unexpected error: {error}"


# Main function containing the chatbot logic
def main():
    """Run the chatbot."""

    try:
        # Create OpenAI client
        client = create_client()

    # Handle missing API key or configuration issues
    except ValueError as error:
        print(f"Configuration error: {error}")
        return

    # Handle unexpected startup errors
    except Exception as error:
        print(f"Unexpected startup error: {error}")
        return

    # Display startup message
    print("OpenAI chatbot started.")
    print("Type 'exit' or 'quit' to stop.")

    # Infinite loop keeps the chatbot running
    while True:
        try:
            # Ask the user for input
            prompt = input("\nSkriv havd er det din hjerne: ").strip()

            # Prevent empty messages
            if not prompt:
                print("Please enter a message.")
                continue

            # Exit condition
            if prompt.lower() in ["quit", "exit"]:
                print("Goodbye!")
                break

            # Generate AI response
            response = generate_response(client, prompt)

            # Display response
            print("\nAssistant:")
            print(response)

        # Handle Ctrl + C gracefully
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        # Catch any unexpected runtime errors
        except Exception as error:
            print(f"Unexpected error: {error}")


# This ensures the program only runs when executed directly
# and not when imported into another Python file
if __name__ == "__main__":
    main()
