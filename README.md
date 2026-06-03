# OpenAI Chatbot

A simple command-line chatbot built with the OpenAI Python SDK.

## Overall Flow

```text
Start Program
      ↓
Create OpenAI Client
      ↓
Ask User For Input
      ↓
Send Input To GPT
      ↓
Receive Response
      ↓
Display Response
      ↓
Ask Again
      ↓
Type "exit" to quit
```

## How It Works

1. The program starts and creates an OpenAI client.
2. The user enters a question or prompt.
3. The prompt is sent to the OpenAI model.
4. The model generates a response.
5. The response is displayed in the terminal.
6. The program continues to ask for new prompts until the user types `exit` or `quit`.

## Example Session

```text
You: What is Python?

Assistant:
Python is a high-level programming language used for web development,
data science, automation, and AI.

You: Give me an example of a list

Assistant:
numbers = [1, 2, 3, 4, 5]

You: exit
```

## Requirements

* Python 3.10+
* OpenAI Python SDK

Install dependencies:

```bash
pip install openai python-dotenv
```

## Running the Application

Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your_api_key"
```

Run the chatbot:

```bash
python openai_chatbot.py
```

To exit the application, type:

```text
exit
```

or

```text
quit
```
