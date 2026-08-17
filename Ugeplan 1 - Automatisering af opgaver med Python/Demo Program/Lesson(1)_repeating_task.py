from dotenv import load_dotenv
from openai import OpenAI

from generic_llm_client_interface import AIService, GeminiClient, OpenAIClient


def run_openai_example():
    client = OpenAI()
    llm = OpenAIClient(client)
    ai = AIService(llm)
    ai.print_response("Explain Python automation in simple words.")


def run_gemini_example():
    try:
        from google import genai
    except ImportError:
        print("\nGemini setup error: google-genai is not installed.")
        print("Install dependencies with: python -m pip install -r requirements.txt")
        print("-" * 80)
        return

    client = genai.Client()
    llm = GeminiClient(client)
    ai = AIService(llm)
    ai.print_response("Explain Python automation in simple words.")


def run_list_examples():
    list_of_tasks = [
        "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
        "Write a birthday poem for Otto, celebrating his 28th birthday.",
        "Write a 300-word review of the movie 'The Arrival'.",
    ]
    print(list_of_tasks)

    for task in list_of_tasks:
        print(task)

    for task in list_of_tasks:
        pass
        # print_llm_response(task)

    # Iteratively updating AI prompts using lists
    ice_cream_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

    for flavor in ice_cream_flavors:
        prompt = f"""For the ice cream flavor listed below,
        provide a captivating description that could be used for promotional purposes.
        Flavor: {flavor}
        """
        print(prompt)
        # print_llm_response(prompt)

    promotional_descriptions = []
    for flavor in ice_cream_flavors:
        prompt = f"""For the ice cream flavor listed below,
        provide a captivating description that could be used for promotional purposes.

        Flavor: {flavor}

        """
        print(prompt)
        # description = get_llm_response(prompt)
        # promotional_descriptions.append(description)

    print(promotional_descriptions)

    # Fix the following code.
    # It should print the flavors in
    # ice_cream_flavors one by one.
    ice_cream_flavors = ["Chocolate", "Mint Chocolate Chip"]

    for flavor in ice_cream_flavors:
        print(flavor)

    # Translate the flavors in ice_cream_flavors to Spanish.
    ice_cream_flavors = ["Vanilla", "Strawberry"]

    for flavor in ice_cream_flavors:
        prompt = f"""For the ice cream flavor listed below,
        translate it to Spanish.

        Flavor: {flavor}
        """
        print(prompt)
        # print_llm_response(prompt)


def main():
    load_dotenv()
    run_openai_example()
    run_gemini_example()
    run_list_examples()


if __name__ == "__main__":
    main()
