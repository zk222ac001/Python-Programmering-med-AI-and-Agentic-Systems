# Before running the program, install Ollama and the
# Python package, then download the model:
# -----------------------
# ollama pull llama3.2
# pip install ollama
# ----------------------
# test that Ollama works with:
# -----------------------
# ollama run llama3.2
# -----------------------
# Run your Python program:
# Enter a programming topic: Python functions
# Ollama Python library

from ollama import chat

topic = input("Enter a programming topic: ")

prompt = f"""
You are a programming teacher.

Teach the following topic:

Topic:
{topic}

Student level:
Beginner

Requirements:
1. Give a simple definition.
2. Give a real-world analogy.
3. Give one Python example.
4. Explain the example.
5. Give two exercises.
"""

response = chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])

print("\nAI Teacher")
print("----------------------")
print(response.message.content)
