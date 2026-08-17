'''
For completely free testing, use Ollama,
which runs an AI model locally on your Windows computer—no API credits required.
Install Ollama for Windows.
Open PowerShell and download a small model:
ollama run gemma3:1b
'''

# Import OpenAI because Ollama exposes an OpenAI-compatible local API.
from openai import OpenAI

# Import OpenAIError so connection/API problems can be handled cleanly.
from openai import OpenAIError

# Create a client that points to the local Ollama server instead of OpenAI.
client = OpenAI(
    # Ollama's OpenAI-compatible endpoint runs locally on port 11434.
    base_url="http://localhost:11434/v1",
    # Ollama requires a value here, but it is not a real OpenAI key.
    api_key="ollama",  # Required by the library, but not a real key
    # Stop waiting after 10 seconds if Ollama is unavailable.
    timeout=10.0,
    # Disable retries so setup errors appear quickly.
    max_retries=0,
)

# Send one chat-completion request to the local Ollama model.
try:
    # Ask the local model to explain Python.
    response = client.chat.completions.create(
        model="gemma3:1b",
        messages=[
            {"role": "user", "content": "Explain Python in simple words"}
        ]
    )

    # Print the assistant message returned by Ollama.
    print(response.choices[0].message.content)

# Show setup help if Ollama is not running or the model is missing.
except OpenAIError as error:
    print(f"Ollama Error: {error}")
    print("Make sure Ollama is running and the model is installed:")
    print("ollama run gemma3:1b")

'''
Ollama officially provides an OpenAI-compatible API,
so your existing code may require only small changes.
This is free, but:
The model runs on your computer and may be slower.
gemma3:1b is suitable for testing and weaker computers.
Keep Ollama running while executing the Python program.
You don’t need the OPENAI_API_KEY environment variable for this version.
'''
