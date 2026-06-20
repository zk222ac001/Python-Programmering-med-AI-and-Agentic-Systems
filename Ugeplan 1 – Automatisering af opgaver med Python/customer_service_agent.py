from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are a friendly customer service AI agent.

Rules:
- Be polite and professional.
- Help customers solve their issues.
- Ask follow-up questions when needed.
- Provide step-by-step instructions.
- If the issue cannot be solved, recommend escalation to a human agent.
"""

messages: list[ChatCompletionMessageParam] = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("Customer Service Agent")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Customer: ")

    if user_input.lower() in ("exit", "quit"):
        print("Agent: Goodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=500,
        )

        agent_reply = response.choices[0].message.content or ""

        messages.append(
            {
                "role": "assistant",
                "content": agent_reply
            }
        )

        print(f"\nAgent: {agent_reply}\n")

    except Exception as e:
        print(f"\nError: {e}\n")