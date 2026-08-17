"""Interactive customer-service chatbot demo using the OpenAI Chat Completions API."""

# Import the OpenAI client used to send requests to the API.
from openai import OpenAI

# Import the message type so the conversation list has a clear structure.
from openai.types.chat import ChatCompletionMessageParam

# Import dotenv so API keys can be loaded from a local .env file.
from dotenv import load_dotenv


# Load environment variables such as OPENAI_API_KEY from the .env file.
load_dotenv()

# Create the OpenAI client after the environment variables are loaded.
client = OpenAI()

# Define the system prompt that controls the assistant's customer-service behavior.
SYSTEM_PROMPT = """
You are a friendly customer service AI agent.

Rules:
- Be polite and professional.
- Help customers solve their issues.
- Ask follow-up questions when needed.
- Provide step-by-step instructions.
- If the issue cannot be solved, recommend escalation to a human agent.
"""

# Store the full conversation history that will be sent with every request.
messages: list[ChatCompletionMessageParam] = [
    {
        # The system role gives the model long-running behavior instructions.
        "role": "system",
        # The content is the customer-service policy written above.
        "content": SYSTEM_PROMPT
    }
]

# Print a simple heading so the user knows the chatbot has started.
print("Customer Service Agent")

# Tell the user how to stop the interactive loop.
print("Type 'exit' to quit.\n")

# Keep asking for customer input until the user exits.
while True:
    # Read one message from the customer in the terminal.
    user_input = input("Customer: ")

    # Stop the chatbot if the customer types an exit command.
    if user_input.lower() in ("exit", "quit"):
        print("Agent: Goodbye!")
        break

    # Add the customer's new message to the conversation history.
    messages.append(
        {
            # The user role tells the model this message came from the customer.
            "role": "user",
            # The content is the exact text typed by the customer.
            "content": user_input
        }
    )

    # Send the conversation to OpenAI and handle any API/runtime problems.
    try:
        # Ask the model to generate the next assistant message.
        response = client.chat.completions.create(
            # Select the model used for this demo.
            model="gpt-4o-mini",
            # Send the full message history so the model has context.
            messages=messages,
            # Limit the response length so the assistant does not ramble.
            max_tokens=500,
        )

        # Extract the assistant text; fall back to an empty string if no text appears.
        agent_reply = response.choices[0].message.content or ""

        # Save the assistant response so future turns include it as context.
        messages.append(
            {
                # The assistant role marks this as the model's previous answer.
                "role": "assistant",
                # The content is the generated answer.
                "content": agent_reply
            }
        )

        # Display the assistant reply in the terminal.
        print(f"\nAgent: {agent_reply}\n")

    # Print any error without crashing the entire chat loop.
    except Exception as e:
        print(f"\nError: {e}\n")
