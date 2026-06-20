from openai import OpenAI
import os

# const variables
MODEL_NAME = "gpt-5"
GENERIC_KEY = os.getenv("OPENAI_API_KEY")


# Initialize OpenAI client
client = OpenAI(api_key=GENERIC_KEY)


def get_llm_response(prompt):
    """Send prompt to OpenAI and return response."""
    response = client.responses.create(model=MODEL_NAME, input=prompt)
    return response.output_text


def print_llm_response(prompt):
    """Print AI response."""
    print("\nPROMPT:")
    print(prompt)

    print("\nRESPONSE:")
    print(get_llm_response(prompt))
    print("-" * 80)


# ==========================================
# Example 1: Task List
# ==========================================

list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'Arrival'.",
]

print("\n=== TASK EXAMPLES ===\n")

for task in list_of_tasks:
    print_llm_response(task)


# ==========================================
# Example 2: Ice Cream Descriptions
# ==========================================

ice_cream_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

print("\n=== ICE CREAM DESCRIPTIONS ===\n")

for flavor in ice_cream_flavors:
    prompt = f"""
For the ice cream flavor listed below,
provide a captivating description that could be used for promotional purposes.

Flavor: {flavor}
"""
    print_llm_response(prompt)

# ==========================================
# Example 3: Save AI Results to a List
# ==========================================

promotional_descriptions = []

for flavor in ice_cream_flavors:
    prompt = f"""
For the ice cream flavor listed below,
provide a captivating description that could be used for promotional purposes.

Flavor: {flavor}
"""

    description = get_llm_response(prompt)
    promotional_descriptions.append(description)

print("\n=== SAVED DESCRIPTIONS ===\n")

for desc in promotional_descriptions:
    print(desc)
    print()


# ==========================================
# Exercise 1 - Fixed
# ==========================================

print("\n=== EXERCISE 1 ===\n")

ice_cream_flavors = ["Chocolate", "Mint Chocolate Chip"]

for flavor in ice_cream_flavors:
    print(flavor)


# ==========================================
# Exercise 2 - Translate to Spanish
# ==========================================

print("\n=== EXERCISE 2 ===\n")

ice_cream_flavors = ["Vanilla", "Strawberry"]

for flavor in ice_cream_flavors:
    prompt = f"""
Translate the following ice cream flavor to Spanish.
Provide only the translation.

Flavor: {flavor}
"""

    print_llm_response(prompt)


# ==========================================
# Exercise 3 - Correct Typos
# ==========================================

print("\n=== EXERCISE 3 ===\n")

words_with_typos = ["Aple", "Wether", "Newpaper"]
words_without_typos = []

for word in words_with_typos:
    prompt = f"""
Fix the spelling mistake in the following word: {word}
Provide only the corrected word.
"""

    correct_word = get_llm_response(prompt).strip()
    words_without_typos.append(correct_word)

print("Corrected words:")
print(words_without_typos)
