'''
This imports the chat function from the Ollama Python library.
The chat() function allows Python to communicate with an Ollama language model.
It can send:
-A model name
-System instructions
-User messages
-Previous conversation messages
-Model options

Before using this import, install the library:
'''
# pip install ollama


# 1. Import the Ollama client
from ollama import Client, ResponseError

# Create an Ollama client with a timeout so connection problems fail quickly.
client = Client(timeout=10)


# 2. Define a reusable function
def create_explanation(topic: str, level: str) -> str:
    # 3. Build the prompt
    user_input = f"""
    Explain {topic} to a {level} student.
    """

    # 4. Send the prompt to the local model
    response = client.chat(
        model="llama3.2",
        messages=[
            {
                # The system message controls the teacher-like behavior.
                "role": "system",
                "content": "You are a programming teacher.",
            },
            {
                # The user message contains the topic and learner level.
                "role": "user",
                "content": user_input,
            },
        ],
    )

    # 5. Extract the generated text
    content = response.message.content

    # 6. Check that text was returned
    if content is None:
        raise RuntimeError("Ollama returned an empty response.")

    # 7. Return the text
    return content


# 8. Call the function and display its result
try:
    # Generate and print a beginner explanation about dictionaries.
    print(create_explanation("Python dictionaries", "beginner"))

# Handle model-specific Ollama errors, such as a missing model.
except ResponseError as error:
    print(f"Ollama model error: {error}")
    print("Make sure the model is installed:")
    print("ollama run llama3.2")

# Handle connection errors, timeouts, or other local setup issues.
except Exception as error:
    print(f"Ollama connection error: {error}")
    print("Make sure Ollama is running before executing this program.")
