'''
For completely free testing, use Ollama, 
which runs an AI model locally on your Windows computer—no API credits required.
Install Ollama for Windows.
Open PowerShell and download a small model:
ollama run gemma3:1b
'''
from openai import OpenAI
from openai import OpenAIError

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Required by the library, but not a real key
    timeout=10.0,
    max_retries=0,
)

try:
    response = client.chat.completions.create(
        model="gemma3:1b",
        messages=[
            {"role": "user", "content": "Explain Python in simple words"}
        ]
    )
    print(response.choices[0].message.content)
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
