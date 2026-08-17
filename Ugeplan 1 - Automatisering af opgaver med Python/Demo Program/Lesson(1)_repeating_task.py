"""Lesson demo for repeating tasks with lists and AI prompts."""

# Import dotenv so the API keys in .env are available to provider clients.
from dotenv import load_dotenv

# Import the OpenAI client used in the OpenAI example.
from openai import OpenAI

# Import the shared service and provider wrappers used by the examples.
from generic_llm_client_interface import AIService, GeminiClient, OpenAIClient


# Run the OpenAI version of the prompt example.
def run_openai_example():
    # Create the provider-specific OpenAI client.
    client = OpenAI()

    # Wrap the provider client in the shared interface.
    llm = OpenAIClient(client)

    # Create a service that can ask the wrapped client questions.
    ai = AIService(llm)

    # Send one demo prompt and print the formatted response.
    ai.print_response("Explain Python automation in simple words.")


# Run the Gemini version of the prompt example.
def run_gemini_example():
    # Import Gemini only when this example runs, so missing packages do not stop the whole lesson.
    try:
        from google import genai

    # Show a friendly setup message if google-genai is not installed.
    except ImportError:
        print("\nGemini setup error: google-genai is not installed.")
        print("Install dependencies with: python -m pip install -r requirements.txt")
        print("-" * 80)
        return

    # Create the provider-specific Gemini client.
    client = genai.Client()

    # Wrap the provider client in the shared interface.
    llm = GeminiClient(client)

    # Create a service that can ask the wrapped client questions.
    ai = AIService(llm)

    # Send one demo prompt and print the formatted response.
    ai.print_response("Explain Python automation in simple words.")


# Run examples that show how loops can repeat prompt-building tasks.
def run_list_examples():
    # Store several natural-language tasks in a Python list.
    list_of_tasks = [
        "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
        "Write a birthday poem for Otto, celebrating his 28th birthday.",
        "Write a 300-word review of the movie 'The Arrival'.",
    ]

    # Print the full list at once.
    print(list_of_tasks)

    # Print each task one by one.
    for task in list_of_tasks:
        print(task)

    # This loop is a placeholder for sending each task to an LLM.
    for task in list_of_tasks:
        pass
        # print_llm_response(task)

    # Iteratively updating AI prompts using lists
    ice_cream_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

    # Build a promotional prompt for each flavor.
    for flavor in ice_cream_flavors:
        # Insert the current flavor into the prompt with an f-string.
        prompt = f"""For the ice cream flavor listed below,
        provide a captivating description that could be used for promotional purposes.
        Flavor: {flavor}
        """

        # Print the prompt so learners can inspect how it changes.
        print(prompt)
        # print_llm_response(prompt)

    # Create a list that could store AI-generated descriptions.
    promotional_descriptions = []

    # Build prompts again, this time showing where saved results would be collected.
    for flavor in ice_cream_flavors:
        # Insert the current flavor into a multi-line prompt.
        prompt = f"""For the ice cream flavor listed below,
        provide a captivating description that could be used for promotional purposes.

        Flavor: {flavor}

        """

        # Print the prompt instead of calling an LLM in this lesson step.
        print(prompt)
        # description = get_llm_response(prompt)
        # promotional_descriptions.append(description)

    # Print the list of saved descriptions, which is still empty in this demo.
    print(promotional_descriptions)

    # Fix the following code.
    # It should print the flavors in
    # ice_cream_flavors one by one.
    ice_cream_flavors = ["Chocolate", "Mint Chocolate Chip"]

    # Loop through the flavors and print each item.
    for flavor in ice_cream_flavors:
        print(flavor)

    # Translate the flavors in ice_cream_flavors to Spanish.
    ice_cream_flavors = ["Vanilla", "Strawberry"]

    # Build one translation prompt for each flavor.
    for flavor in ice_cream_flavors:
        # Ask clearly for a Spanish translation of the current flavor.
        prompt = f"""For the ice cream flavor listed below,
        translate it to Spanish.

        Flavor: {flavor}
        """

        # Print the prompt so learners can see the final prompt text.
        print(prompt)
        # print_llm_response(prompt)


# Run the lesson examples in a clear order.
def main():
    # Load API keys from .env before creating provider clients.
    load_dotenv()

    # Run the OpenAI demo first.
    run_openai_example()

    # Run the Gemini demo second.
    run_gemini_example()

    # Run the list and loop examples last.
    run_list_examples()


# Start the lesson only when this file is executed directly.
if __name__ == "__main__":
    main()
