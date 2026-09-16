# 🧪 Classroom Exercise 1 – Bad Prompt → Better Prompt

## 🎯 Learning Objective

The purpose of this exercise is to help students understand how a **simple or vague prompt** can be improved by adding structure, context, and clear requirements.

Students will transform a **bad prompt** into a **better structured prompt** using five important prompt-engineering elements:

* 👤 **ROLE**
* 🎯 **TASK**
* 📚 **CONTEXT**
* ✅ **REQUIREMENTS**
* 📄 **OUTPUT FORMAT**

---

## ❌ Step 1 – Start with a Bad Prompt

Give students the following prompt:

```text
Explain functions.
```

Ask students:

> Is this prompt clear enough for an AI model?

The prompt does not specify:

* Which programming language?
* Who the learner is?
* What level of explanation is required?
* Whether examples should be included?
* How the answer should be structured?

Because of this, the AI model must make several assumptions.

---

## 🧠 Step 2 – Improve the Prompt

Students must rewrite the prompt using the following structure:

```text
ROLE
TASK
CONTEXT
REQUIREMENTS
OUTPUT FORMAT
```

---

## ✅ Step 3 – Example of an Improved Prompt

```text
ROLE:
You are a Python teacher.

TASK:
Explain Python functions.

CONTEXT:
The student understands variables and loops
but has never used functions.

REQUIREMENTS:
Use simple language.
Give one real-world analogy.
Provide one Python example.

OUTPUT FORMAT:
Definition
Analogy
Code
Explanation
Exercise
```

---

## 🔍 Understanding the Prompt Structure

### 👤 ROLE

The **ROLE** tells the AI who it should act as.

Example:

```text
You are a Python teacher.
```

This helps the AI choose an appropriate teaching style.

---

### 🎯 TASK

The **TASK** clearly describes what the AI should do.

Example:

```text
Explain Python functions.
```

Instead of simply saying:

```text
Explain functions.
```

we specify that the topic is **Python functions**.

---

### 📚 CONTEXT

The **CONTEXT** provides information about the learner or situation.

Example:

```text
The student understands variables and loops
but has never used functions.
```

This helps the AI adjust the explanation to the student's knowledge level.

---

### ✅ REQUIREMENTS

The **REQUIREMENTS** tell the AI what must be included.

Example:

```text
Use simple language.
Give one real-world analogy.
Provide one Python example.
```

Requirements make the response more predictable and useful.

---

### 📄 OUTPUT FORMAT

The **OUTPUT FORMAT** tells the AI how the answer should be organized.

Example:

```text
Definition
Analogy
Code
Explanation
Exercise
```

The AI now knows exactly how to structure the response.

---

# 🔬 Step 4 – Compare the Two Prompts

## Prompt A – Bad Prompt

```text
Explain functions.
```

## Prompt B – Improved Prompt

```text
ROLE:
You are a Python teacher.

TASK:
Explain Python functions.

CONTEXT:
The student understands variables and loops
but has never used functions.

REQUIREMENTS:
Use simple language.
Give one real-world analogy.
Provide one Python example.

OUTPUT FORMAT:
Definition
Analogy
Code
Explanation
Exercise
```

---

# 📊 Compare the Outputs

Run both prompts in the same AI model or another model forexample you have infront ** Chatgtp , Claude , Google Gemini or others **.

Students should compare the responses based on:

| Criteria                  | Bad Prompt | Better Prompt |
| ------------------------- | ---------- | ------------- |
| Clear explanation         | ❓          | ✅             |
| Appropriate for beginners | ❓          | ✅             |
| Python-specific           | ❓          | ✅             |
| Real-world analogy        | ❌          | ✅             |
| Code example              | ❓          | ✅             |
| Structured answer         | ❌          | ✅             |
| Exercise included         | ❌          | ✅             |

---

# 💬 Classroom Discussion

Ask students the following questions:

1. Which prompt produced the better answer?
2. Why was the second answer more structured?
3. How did the **ROLE** affect the response?
4. How did **CONTEXT** change the explanation?
5. Why are **REQUIREMENTS** useful?
6. What happened when an **OUTPUT FORMAT** was specified?
7. Could the prompt be improved even further?

---

# 🎓 Key Learning Point

A vague prompt forces the AI model to **guess what the user wants**.

A structured prompt gives the AI:

* a clear role,
* a specific task,
* relevant context,
* clear requirements,
* and a desired output structure.

Therefore:

> **Better instructions usually produce better and more predictable AI responses.**
