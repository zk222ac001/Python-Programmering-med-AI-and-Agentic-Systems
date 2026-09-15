# 🧪 Classroom Exercise 3 – Create an AI Study Assistant

## 🎯 Learning Objective

The purpose of this exercise is to help students understand how **Python variables** can be used to collect user input and dynamically create a prompt for an LLM.

Students will build a simple **AI Study Assistant**.

The program should:

1. Ask the user for information.
2. Store the information in Python variables.
3. Generate a structured prompt.
4. Send the prompt to an LLM.
5. Display the generated study material.

---

# 📝 Step 1 – Ask the User for Input

The Python program should ask the user for:

```text
Topic:
Level:
Language:
Number of exercises:
```

---

## Example User Input

```text
Topic: Python loops
Level: Beginner
Language: English
Number of exercises: 3
```

---

# 🔄 System Workflow

The program should follow this process:

```text
Student Input
      │
      ▼
Python Variables
      │
      ▼
Prompt Template
      │
      ▼
LLM
      │
      ▼
Study Material
```

---

# 🐍 Step 2 – Store the Input in Python Variables

Students should create variables for:

```text
topic
level
language
number_of_exercises
```

For example:

```python
topic = input("Enter topic: ")
level = input("Enter student level: ")
language = input("Enter language: ")
number_of_exercises = input("Enter number of exercises: ")
```

---

# 🧠 Step 3 – Generate the Prompt with Python

Python should dynamically create the prompt using the information entered by the user.

A possible prompt structure is:

```text
ROLE:
You are an experienced programming teacher.

TASK:
Teach the following topic:
{topic}

CONTEXT:
The student level is:
{level}

LANGUAGE:
Explain everything in:
{language}

REQUIREMENTS:
- Give a simple definition.
- Explain the concept step by step.
- Give one real-world analogy.
- Provide practical examples.
- Generate {number_of_exercises} exercises.

OUTPUT FORMAT:
1. Definition
2. Explanation
3. Real-world analogy
4. Examples
5. Exercises
```

---

# 💻 Step 4 – Create the Prompt Template in Python

Students can use an **f-string** to insert the Python variables into the prompt.

```python
prompt = f"""
ROLE:
You are an experienced programming teacher.

TASK:
Teach the following topic:
{topic}

CONTEXT:
Student level:
{level}

LANGUAGE:
{language}

REQUIREMENTS:
- Give a simple definition.
- Explain the concept step by step.
- Give one real-world analogy.
- Provide practical examples.
- Generate {number_of_exercises} exercises.

OUTPUT FORMAT:
1. Definition
2. Explanation
3. Real-world analogy
4. Examples
5. Exercises
"""
```

---

# 🔍 Step 5 – Display the Generated Prompt

Before connecting the program to an LLM, students should test whether Python generates the correct prompt.

```python
print("\nGenerated Prompt")
print("-----------------------------")
print(prompt)
```

---

# ✅ Example Generated Prompt

If the student enters:

```text
Topic: Python loops
Level: Beginner
Language: English
Number of exercises: 3
```

Python should generate something similar to:

```text
ROLE:
You are an experienced programming teacher.

TASK:
Teach the following topic:
Python loops

CONTEXT:
Student level:
Beginner

LANGUAGE:
English

REQUIREMENTS:
- Give a simple definition.
- Explain the concept step by step.
- Give one real-world analogy.
- Provide practical examples.
- Generate 3 exercises.

OUTPUT FORMAT:
1. Definition
2. Explanation
3. Real-world analogy
4. Examples
5. Exercises
```

---

# 🤖 Step 6 – Send the Prompt to an LLM

After verifying the generated prompt, connect the Python program to an LLM.

The complete workflow becomes:

```text
┌───────────────────────┐
│     Student Input     │
│                       │
│ Topic                 │
│ Level                 │
│ Language              │
│ Number of Exercises   │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Python Variables    │
│                       │
│ topic                 │
│ level                 │
│ language              │
│ number_of_exercises   │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    Prompt Template    │
│                       │
│ ROLE                  │
│ TASK                  │
│ CONTEXT               │
│ REQUIREMENTS          │
│ OUTPUT FORMAT         │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│          LLM          │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    Study Material     │
│                       │
│ Explanation           │
│ Examples              │
│ Exercises             │
└───────────────────────┘
```

---

# 🎯 Student Task

Create a Python program that asks the user for:

```text
Topic
Level
Language
Number of exercises
```

The program must then:

1. Store the information in variables.
2. Generate a structured prompt.
3. Use the following prompt components:

```text
ROLE
TASK
CONTEXT
REQUIREMENTS
OUTPUT FORMAT
```

4. Print the generated prompt.
5. Send the prompt to an LLM.
6. Display the generated study material.

---

# 🧪 Test Cases

Students should test the program with different inputs.

## Test 1

```text
Topic: Python loops
Level: Beginner
Language: English
Number of exercises: 3
```

## Test 2

```text
Topic: Object-Oriented Programming
Level: Intermediate
Language: Danish
Number of exercises: 5
```

## Test 3

```text
Topic: Cybersecurity
Level: Beginner
Language: English
Number of exercises: 4
```

## Test 4

```text
Topic: Raspberry Pi GPIO
Level: Intermediate
Language: Danish
Number of exercises: 3
```

---

# ⭐ Challenge Task

Extend the program by asking the student for additional information:

```text
Topic:
Level:
Language:
Number of exercises:
Learning style:
Programming language:
Include code examples?:
```

Use these values to make the generated prompt even more personalized.

---

# 💡 Key Learning Point

This exercise demonstrates an important concept in AI application development:

> **A prompt does not always have to be written manually. Python can dynamically generate prompts using user input.**

The basic architecture is:

```text
User Input
    ↓
Python Variables
    ↓
Dynamic Prompt
    ↓
LLM
    ↓
AI-Generated Content
```

This is the foundation for building applications such as:

* 🤖 AI Study Assistants
* 🧑‍🏫 AI Tutors
* 💻 Programming Assistants
* 🔐 Cybersecurity Assistants
* 📊 Data Analysis Assistants
* 🛠️ Technical Support Assistants
* 🤖 Robotics Learning Assistants
