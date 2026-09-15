# 🤖 AI Programming Tutor

## 📘 Scenario

Your college wants to develop a simple **AI Programming Tutor** that helps first-semester programming students understand Python topics.

Your task is to build the **first prototype** of this AI assistant.

The application should collect information from the student, generate a structured prompt, send the prompt to an LLM, and display personalized learning material.

---

# 🎯 Learning Objectives

After completing this exercise, students should be able to:

* Collect user input with Python.
* Store input in variables.
* Create a dynamic prompt using Python.
* Use a structured prompt template.
* Send a prompt to an LLM.
* Generate personalized programming learning material.

---

# 📝 Program Requirements

The program should ask the user for the following information:

```text
Programming topic
Student level
Preferred language
Number of exercises
```

---

# 💻 Example User Input

```text
Programming topic: Functions

Student level: Beginner

Preferred language: English

Number of exercises: 3
```

---

# 🧠 Expected AI Output

The AI Programming Tutor should generate:

```text
1. Topic definition

2. Simple explanation

3. Real-world analogy

4. Python example

5. Code explanation

6. Common mistakes

7. Exercises
```

---

# 🔄 Application Workflow

```text
Student
   │
   ▼
User Input
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
AI Programming Tutor
   │
   ▼
Learning Material
```

---

# 🐍 Step 1 – Collect User Input

Create Python variables for the information entered by the student.

```python
topic = input("Enter programming topic: ")

level = input("Enter student level: ")

language = input("Enter preferred language: ")

number_of_exercises = input("Enter number of exercises: ")
```

---

# 🧩 Step 2 – Create a Structured Prompt

The application should dynamically generate a prompt using the student's input.

Use the following prompt structure:

```text
ROLE
TASK
CONTEXT
REQUIREMENTS
OUTPUT FORMAT
```

---

# ✨ Example Prompt Template

```text
ROLE:
You are an experienced Python programming teacher.

TASK:
Teach the following Python topic:

{topic}

CONTEXT:
The student level is:

{level}

The preferred language is:

{language}

REQUIREMENTS:
- Use simple language appropriate for the student's level.
- Explain the concept clearly.
- Give one real-world analogy.
- Provide one Python example.
- Explain the code step by step.
- Explain common mistakes.
- Generate {number_of_exercises} exercises.

OUTPUT FORMAT:

1. Topic Definition
2. Simple Explanation
3. Real-World Analogy
4. Python Example
5. Code Explanation
6. Common Mistakes
7. Exercises
```

---

# 🐍 Step 3 – Generate the Prompt with Python

Use an **f-string** to insert the student's input into the prompt.

```python
prompt = f"""
ROLE:
You are an experienced Python programming teacher.

TASK:
Teach the following Python topic:

{topic}

CONTEXT:
Student level:
{level}

Preferred language:
{language}

REQUIREMENTS:
- Use simple language appropriate for the student's level.
- Explain the concept clearly.
- Give one real-world analogy.
- Provide one Python example.
- Explain the code step by step.
- Explain common mistakes.
- Generate {number_of_exercises} exercises.

OUTPUT FORMAT:
1. Topic Definition
2. Simple Explanation
3. Real-World Analogy
4. Python Example
5. Code Explanation
6. Common Mistakes
7. Exercises
"""
```

---

# 🔍 Step 4 – Test the Generated Prompt

Before connecting the application to an LLM, print the generated prompt.

```python
print("\nGenerated Prompt")
print("--------------------------------")
print(prompt)
```

---

# ✅ Example Generated Prompt

If the student enters:

```text
Programming topic: Functions
Student level: Beginner
Preferred language: English
Number of exercises: 3
```

The application could generate:

```text
ROLE:
You are an experienced Python programming teacher.

TASK:
Teach the following Python topic:

Functions

CONTEXT:
Student level:
Beginner

Preferred language:
English

REQUIREMENTS:
- Use simple language appropriate for the student's level.
- Explain the concept clearly.
- Give one real-world analogy.
- Provide one Python example.
- Explain the code step by step.
- Explain common mistakes.
- Generate 3 exercises.

OUTPUT FORMAT:
1. Topic Definition
2. Simple Explanation
3. Real-World Analogy
4. Python Example
5. Code Explanation
6. Common Mistakes
7. Exercises
```

---

# 📖 Example Expected Output

## 1. Topic Definition

A **function** is a reusable block of Python code designed to perform a specific task.

---

## 2. Simple Explanation

Instead of writing the same code many times, we can place that code inside a function and call the function whenever we need it.

---

## 3. Real-World Analogy

Think about a **coffee machine**.

You press a button and the machine performs several steps:

```text
Button Press
    ↓
Heat Water
    ↓
Add Coffee
    ↓
Pour Coffee
```

You do not need to manually perform every step.

A Python function works in a similar way.

---

## 4. Python Example

```python
def greet():
    print("Hello!")

greet()
```

---

## 5. Code Explanation

```python
def greet():
```

`def` tells Python that we are creating a function.

`greet` is the name of the function.

```python
print("Hello!")
```

This is the code executed when the function runs.

```python
greet()
```

This calls the function.

---

## 6. Common Mistakes

### Forgetting Parentheses

Incorrect:

```python
greet
```

Correct:

```python
greet()
```

### Incorrect Indentation

Incorrect:

```python
def greet():
print("Hello!")
```

Correct:

```python
def greet():
    print("Hello!")
```

---

## 7. Exercises

### Exercise 1

Create a function called:

```python
welcome()
```

The function should print:

```text
Welcome to Python!
```

### Exercise 2

Create a function called:

```python
student_name()
```

The function should print your name.

### Exercise 3

Create a function called:

```python
add_numbers()
```

The function should add two numbers and display the result.

---

# 🧪 Student Assignment

Create an **AI Programming Tutor** in Python.

Your application must:

1. Ask the student for a programming topic.
2. Ask for the student's level.
3. Ask for the preferred language.
4. Ask for the number of exercises.
5. Store the information in Python variables.
6. Generate a structured prompt.
7. Send the prompt to an LLM.
8. Display the generated learning material.

---

# 📋 Minimum Prompt Structure

Your prompt must contain:

```text
ROLE:
...

TASK:
...

CONTEXT:
...

REQUIREMENTS:
...

OUTPUT FORMAT:
...
```

---

# 🧪 Test Your Application

Test your program with at least three different inputs.

## Test 1

```text
Programming topic: Functions
Student level: Beginner
Preferred language: English
Number of exercises: 3
```

## Test 2

```text
Programming topic: Loops
Student level: Beginner
Preferred language: Danish
Number of exercises: 4
```

## Test 3

```text
Programming topic: Object-Oriented Programming
Student level: Intermediate
Preferred language: English
Number of exercises: 5
```

---

# ⭐ Challenge Tasks

After completing the basic version, extend your application with additional options such as:

```text
Include code examples?:
Include quiz questions?:
Include answers to exercises?:
Learning style:
Difficulty:
Programming language:
```

You could also allow the user to select:

```text
1 - Short explanation
2 - Detailed lesson
3 - Practice exercises
4 - Quiz
5 - Complete lesson
```

---

# 🏗️ System Architecture

```text
┌───────────────────────────┐
│          Student          │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│        User Input         │
│                           │
│ Topic                     │
│ Level                     │
│ Language                  │
│ Number of Exercises       │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│      Python Program       │
│                           │
│ Variables                 │
│ Prompt Template           │
│ f-string                  │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│            LLM            │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│    AI Programming Tutor   │
│                           │
│ Definition                │
│ Explanation               │
│ Analogy                   │
│ Python Example            │
│ Code Explanation          │
│ Common Mistakes           │
│ Exercises                 │
└───────────────────────────┘
```

---

# 🎓 Key Learning Point

This exercise demonstrates how a normal Python application can become an **AI-powered application**.

The basic principle is:

```text
User Input
     ↓
Python Variables
     ↓
Dynamic Prompt
     ↓
LLM
     ↓
Personalized AI Response
```

Instead of creating a fixed lesson for every student, the application dynamically creates learning material based on the student's:

* topic,
* knowledge level,
* preferred language,
* and desired number of exercises.

> **Python + Prompt Engineering + LLM = AI-Powered Application**
