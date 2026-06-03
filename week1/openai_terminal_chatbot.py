"""
OpenAI Terminal Chatbot
Author: Zuhair

Requirements:
pip install openai python-dotenv
"""

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
import os
import time


# Model configuration
MODEL_NAME = "gpt-4o-mini"


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

    try:
        response = client.responses.create(model=MODEL_NAME, input=prompt)

        return response.output_text

    except OpenAIError as error:
        return f"OpenAI API Error: {error}"

    except Exception as error:
        return f"Unexpected Error: {error}"


#  Main chatbot loop.
def main():

    try:
        client = create_client()

    except ValueError as error:
        print(f"\nConfiguration Error: {error}")
        return

    except Exception as error:
        print(f"\nStartup Error: {error}")
        return

    print("=" * 50)
    print("🤖 OpenAI Chatbot Started")
    print(f"Model: {MODEL_NAME}")
    print("Type 'exit' or 'quit' to stop")
    print("=" * 50)

    while True:
        try:
            # Get user input
            prompt = input("\nPlease enter a message: ").strip()

            # Validate empty input
            if not prompt:
                print("Please enter a message.")
                continue

            # Exit condition
            if prompt.lower() in ["exit", "quit"]:
                print("\n👋 Goodbye!")
                break

            # Show thinking message
            print("\n⏳ Assistant is thinking...")

            # Start timer
            start_time = time.time()

            # Generate response
            response = generate_response(client, prompt)

            # Calculate processing time
            processing_time = time.time() - start_time

            # Display response
            print("\n🤖 Assistant:")
            print(response)

            # Display processing time
            print(f"\n⏱ Response generated in {processing_time:.2f} seconds")

        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break

        except Exception as error:
            print(f"\nUnexpected Error: {error}")


# Entry point
if __name__ == "__main__":
    main()
