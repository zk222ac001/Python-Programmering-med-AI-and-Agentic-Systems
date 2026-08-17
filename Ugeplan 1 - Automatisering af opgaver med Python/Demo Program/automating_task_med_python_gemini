"""Examples showing repeated prompting tasks with the Gemini API."""

# Import the Gemini SDK client.
from google import genai

# Import dotenv so API keys can be loaded from .env.
from dotenv import load_dotenv

# Import os so environment variables can be read.
import os

# Import sys so the script can exit early when setup is missing.
import sys

# Load variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Stop the script if the required Gemini key is missing.
if not api_key:
    print("ERROR: GEMINI_API_KEY not found.")
    print("Create a .env file and add:")
    print("GEMINI_API_KEY=your_api_key_here")
    sys.exit(1)

# Initialize Gemini client
client = genai.Client(api_key=api_key)


# Send one prompt to Gemini and return the generated text.
def get_llm_response(prompt):
    """Send prompt to Gemini and return response."""

    # Keep API errors readable for beginners.
    try:
        # Ask Gemini to generate content using the selected model.
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        # Return Gemini's generated text.
        return response.text

    # Return an error string instead of crashing the script.
    except Exception as e:
        return f"Error: {e}"


# Print a prompt and the Gemini response in a consistent format.
def print_llm_response(prompt):
    """Print prompt and Gemini response."""

    # Label the prompt section.
    print("\nPROMPT:")

    # Print the prompt that will be sent to Gemini.
    print(prompt)

    # Label the response section.
    print("\nRESPONSE:")

    # Generate and print the response.
    print(get_llm_response(prompt))

    # Separate examples visually.
    print("-" * 80)


# ==========================================
# Example 1: Task List
# ==========================================

# Store several prompts in a list.
list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'Arrival'."
]

# Print a heading for the first example.
print("\n=== TASK EXAMPLES ===\n")

# Send each task prompt to Gemini.
for task in list_of_tasks:
    print_llm_response(task)


# ==========================================
# Example 2: Ice Cream Descriptions
# ==========================================

# Store flavors that will be inserted into a prompt template.
ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip"
]

# Print a heading for the flavor-description example.
print("\n=== ICE CREAM DESCRIPTIONS ===\n")

# Build one prompt per flavor.
for flavor in ice_cream_flavors:
    # Insert the current flavor into a multi-line prompt.
    prompt = f"""
For the ice cream flavor listed below,
provide a captivating description that could be used for promotional purposes.

Flavor: {flavor}
"""

    # Print Gemini's response for the current flavor.
    print_llm_response(prompt)


# ==========================================
# Example 3: Save AI Results To A List
# ==========================================

# Create an empty list for generated descriptions.
promotional_descriptions = []

# Generate and save a description for each flavor.
for flavor in ice_cream_flavors:
    # Reuse the prompt template with a new flavor each time.
    prompt = f"""
For the ice cream flavor listed below,
provide a captivating description that could be used for promotional purposes.

Flavor: {flavor}
"""

    # Get the generated description.
    description = get_llm_response(prompt)

    # Save it in the list.
    promotional_descriptions.append(description)

# Print a heading before displaying saved descriptions.
print("\n=== SAVED DESCRIPTIONS ===\n")

# Print each saved description with a number.
for i, desc in enumerate(promotional_descriptions, start=1):
    print(f"Description {i}:")
    print(desc)
    print()


# ==========================================
# Exercise 1
# ==========================================

# Print a heading for the first exercise.
print("\n=== EXERCISE 1 ===\n")

# Define a short list of flavors.
ice_cream_flavors = ["Chocolate", "Mint Chocolate Chip"]

# Print each flavor one by one.
for flavor in ice_cream_flavors:
    print(flavor)


# ==========================================
# Exercise 2
# ==========================================

# Print a heading for the translation exercise.
print("\n=== EXERCISE 2 ===\n")

# Define the flavors that should be translated.
ice_cream_flavors = ["Vanilla", "Strawberry"]

# Ask Gemini to translate each flavor.
for flavor in ice_cream_flavors:
    # Build a focused translation prompt.
    prompt = f"""
Translate the following ice cream flavor to Spanish.
Provide only the translation.

Flavor: {flavor}
"""

    # Print Gemini's translation response.
    print_llm_response(prompt)


# ==========================================
# Exercise 3
# ==========================================

# Print a heading for the spelling exercise.
print("\n=== EXERCISE 3 ===\n")

# Store words that contain spelling mistakes.
words_with_typos = ["Aple", "Wether", "Newpaper"]

# Create an empty list for corrected words.
words_without_typos = []

# Ask Gemini to correct each word.
for word in words_with_typos:
    # Build a prompt for one spelling correction.
    prompt = f"""
Fix the spelling mistake in the following word: {word}
Provide only the corrected word.
"""

    # Generate and clean the corrected word.
    corrected_word = get_llm_response(prompt).strip()

    # Save the corrected word.
    words_without_typos.append(corrected_word)

# Print the final corrected list.
print("Corrected words:")
print(words_without_typos)
