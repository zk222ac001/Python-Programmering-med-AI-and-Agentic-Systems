# from helper_functions import print_llm_response, get_llm_response

# call Open AI ...............
from openai import OpenAI
from llm_client1 import OpenAIClient, AIService
client = OpenAI()
llm = OpenAIClient(client)
ai = AIService(llm)
ai.print_response("Explain Python automation in simple words.")
# .........................................................
# Call Gemini ...............
from google import genai
from llm_client2 import GeminiClient, AIService

client = genai.Client()

llm = GeminiClient(client)
ai = AIService(llm)

ai.print_response("Explain Python automation in simple words.")
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

# ice cream flavor example
ice_cream_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.
    Flavor: {flavor}
    """
    # print_llm_response(prompt)

# saving results to a list
promotional_descriptions = []
for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.

    Flavor: {flavor}

    """
    # description = get_llm_response(prompt)
    # promotional_descriptions.append(description)

print(promotional_descriptions)


# Fix the following code.
# It should print the flavors in
# ice_cream_flavors one by one.

ice_cream_flavors = ["Chocolate", "Mint Chocolate Chip"]

### EDIT THE FOLLOWING CODE ###
for flavor in ice_cream_flavors:
    print(flavor)
### --------------- ###

# Translate the flavors in ice_cream_flavors to Spanish
ice_cream_flavors = ["Vanilla", "Strawberry"]

for flavor in ice_cream_flavors:
    ### EDIT THE FOLLOWING CODE ###
    # Hint: you only need to add one or two sentences to the prompt
    prompt = f"""For the ice cream flavor listed below, 
    {flavor} translate it to Spanish.
    """
    ### --------------- ###
    # print_llm_response(prompt)
