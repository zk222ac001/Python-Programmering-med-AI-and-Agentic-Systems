"""Examples showing how Python can automate repeated LLM prompting tasks."""

# Import the OpenAI client used to call the Responses API.
# pip install openai
from openai import OpenAI

# Import os so the script can read environment variables.
import os

# Store the ChatGPT model name in one place so it is easy to change later.
MODEL_NAME = "gpt-5"

# Read the OpenAI API key from the environment.
GENERIC_KEY = os.getenv("OPENAI_API_KEY")


# Initialize the OpenAI client with the API key from the environment.
client = OpenAI(api_key=GENERIC_KEY)


def get_llm_response(prompt):
    """Send prompt to OpenAI and return response."""

    # Send the prompt to the selected model.
    response = client.responses.create(model=MODEL_NAME, input=prompt)

    # Return the combined text output from the response.
    return response.output_text


def print_llm_response(prompt):
    """Print AI response."""

    # Show the prompt so the user can compare input and output.
    print("\nPROMPT:")
    print(prompt)

    # Show the model response for this prompt.
    print("\nRESPONSE:")
    print(get_llm_response(prompt))

    # Print a separator between examples.
    print("-" * 80)


# ==========================================
# Example 1: Task List
# ==========================================

# Create a list of prompts that can be processed one by one.
list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'Arrival'.",
]

# Print a heading for the first example.
print("\n=== TASK EXAMPLES ===\n")

# Loop through each task and ask the model to complete it.
for task in list_of_tasks:
    print_llm_response(task)


# ==========================================
# Example 2: Ice Cream Descriptions
# ==========================================

# Store several values that will be inserted into the same prompt template.
ice_cream_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

# Print a heading for the flavor-description example.
print("\n=== ICE CREAM DESCRIPTIONS ===\n")

# Build and send one promotional prompt for each flavor.
for flavor in ice_cream_flavors:
    # Use an f-string so the current flavor is inserted into the prompt.
    prompt = f"""
For the ice cream flavor listed below,
provide a captivating description that could be used for promotional purposes.

Flavor: {flavor}
"""
    # Print the model's response for the current flavor.
    print_llm_response(prompt)

# ==========================================
# Example 3: Save AI Results to a List
# ==========================================

# Create an empty list to collect generated descriptions.
promotional_descriptions = []

# Ask the model for each flavor and store the result.
for flavor in ice_cream_flavors:
    # Reuse the same prompt structure for each list item.
    prompt = f"""
For the ice cream flavor listed below,
provide a captivating description that could be used for promotional purposes.

Flavor: {flavor}
"""

    # Generate the description for the current flavor.
    description = get_llm_response(prompt)

    # Add the generated description to the results list.
    promotional_descriptions.append(description)

# Print a heading before displaying saved results.
print("\n=== SAVED DESCRIPTIONS ===\n")

# Display every saved description.
for desc in promotional_descriptions:
    print(desc)
    print()


# ==========================================
# Exercise 1 - Fixed
# ==========================================

# Print a heading for the first exercise.
print("\n=== EXERCISE 1 ===\n")

# Define a short list of flavors.
ice_cream_flavors = ["Chocolate", "Mint Chocolate Chip"]

# Print each flavor one at a time.
for flavor in ice_cream_flavors:
    print(flavor)


# ==========================================
# Exercise 2 - Translate to Spanish
# ==========================================

# Print a heading for the translation exercise.
print("\n=== EXERCISE 2 ===\n")

# Define the flavors that should be translated.
ice_cream_flavors = ["Vanilla", "Strawberry"]

# Ask the model to translate each flavor.
for flavor in ice_cream_flavors:
    # Build a focused prompt that asks for only the translation.
    prompt = f"""
Translate the following ice cream flavor to Spanish.
Provide only the translation.

Flavor: {flavor}
"""

    # Print the translation response.
    print_llm_response(prompt)


# ==========================================
# Exercise 3 - Correct Typos
# ==========================================

# Print a heading for the typo-correction exercise.
print("\n=== EXERCISE 3 ===\n")

# Store misspelled words that need correction.
words_with_typos = ["Aple", "Wether", "Newpaper"]

# Create an empty list for corrected words.
words_without_typos = []

# Ask the model to correct each word.
for word in words_with_typos:
    # Build a prompt for one spelling correction.
    prompt = f"""
Fix the spelling mistake in the following word: {word}
Provide only the corrected word.
"""

    # Generate and clean the corrected word.
    correct_word = get_llm_response(prompt).strip()

    # Save the corrected word.
    words_without_typos.append(correct_word)

# Display the final list of corrected words.
print("Corrected words:")
print(words_without_typos)
