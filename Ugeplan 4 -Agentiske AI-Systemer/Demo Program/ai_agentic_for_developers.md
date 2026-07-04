# 🤖 Agentic AI for Developers

> Learn how to build AI agents using modern Large Language Models (LLMs), tools, APIs, and agentic workflows.

**Repository:** https://github.com/https-deeplearning-ai/agentic-ai-public

---

# 📖 Overview

This repository accompanies the **DeepLearning.AI Agentic AI** learning materials. It contains practical notebooks, code examples, and hands-on exercises for building intelligent AI agents capable of reasoning, planning, using external tools, and solving complex tasks.

Unlike traditional AI applications that simply generate text, **Agentic AI systems** can:

- 🧠 Reason about problems
- 📋 Create plans
- 🔄 Execute multiple steps
- 🔧 Use external tools
- 🌐 Access APIs
- 📄 Read documents
- 💾 Store memory
- 🤝 Collaborate with other AI agents

---

# 🎯 Learning Objectives

After completing these labs, you will be able to:

- Understand Agentic AI concepts
- Build AI agents using Python
- Work with Large Language Models (LLMs)
- Connect AI to external APIs
- Build multi-step AI workflows
- Create autonomous AI assistants
- Integrate memory into AI agents
- Develop tool-using AI systems

---

# 📂 Repository Structure

```text
agentic-ai-public/
│
├── notebooks/
│   ├── Lesson01.ipynb
│   ├── Lesson02.ipynb
│   ├── Lesson03.ipynb
│   └── ...
│
├── helper_functions/
│
├── images/
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

# 🧠 Topics Covered

## 1. Introduction to Agentic AI

Learn:

- What is Agentic AI?
- Difference between AI Assistants and AI Agents
- Components of an AI Agent
- Agent Architecture

---

## 2. Large Language Models (LLMs)

Topics include:

- Transformers
- Tokens
- Prompt Engineering
- Context Windows
- Embeddings
- Function Calling
- Structured Outputs

Popular LLMs:

- GPT-4
- GPT-5
- Claude
- Gemini
- Llama
- Mistral
- DeepSeek

---

## 3. Prompt Engineering

Learn how to write effective prompts.

Examples:

- Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- Chain-of-Thought prompting
- Role prompting
- Structured prompting

---

## 4. Tool Calling

Teach AI to use external tools.

Examples:

- Weather APIs
- Search engines
- Databases
- Python functions
- File systems
- Calculators

Example Workflow:

```text
User Question
      │
      ▼
 Large Language Model
      │
      ▼
Needs a Tool?
      │
 ┌────┴────┐
 │         │
No         Yes
 │         │
 ▼         ▼
Answer   Call API
           │
           ▼
Receive Result
           │
           ▼
Generate Final Answer
```

---

## 5. AI Memory

Agents can remember information.

Examples:

- Previous conversations
- User preferences
- Task history
- Retrieved documents
- Long-term knowledge

Memory Types

- Short-term Memory
- Long-term Memory
- Vector Memory
- External Database Memory

---

## 6. Planning

Instead of answering immediately, agents can plan.

Example:

```
Goal

↓

Break into Tasks

↓

Solve Each Task

↓

Combine Results

↓

Final Answer
```

---

## 7. Multi-Agent Systems

Multiple AI agents collaborate.

Example:

```text
               User
                 │
                 ▼
          Manager Agent
          /      |      \
         ▼       ▼       ▼
 Research Coding Writing
   Agent    Agent   Agent
         \     |     /
              ▼
       Final Response
```

---

## 8. Retrieval-Augmented Generation (RAG)

Instead of relying only on its training data, an AI agent can retrieve relevant documents before answering.

Workflow:

```text
User Question

↓

Search Knowledge Base

↓

Retrieve Documents

↓

LLM Reads Documents

↓

Generate Accurate Answer
```

Applications:

- Company knowledge bases
- PDFs
- Technical manuals
- Research papers
- Internal documentation

---

## 9. AI Workflows

Examples include:

- Customer Support Agent
- Research Assistant
- Coding Assistant
- Email Assistant
- Financial Analysis
- Healthcare Assistant
- Data Analysis Agent

---

# 💻 Technologies Used

Programming Language

- Python

AI Frameworks

- OpenAI
- Anthropic
- Gemini
- Mistral
- Vertex AI

Libraries

- FastAPI
- Pydantic
- SQLAlchemy
- Requests
- Tavily Search
- Pandas
- Matplotlib
- Scikit-learn

Notebook Environment

- Jupyter Notebook
- VS Code

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/https-deeplearning-ai/agentic-ai-public.git
```

Move into the project directory:

```bash
cd agentic-ai-public
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Launch Jupyter Notebook

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

---

# 📚 Recommended Background Knowledge

Before starting, it helps to have basic knowledge of:

- Python programming
- Object-Oriented Programming (OOP)
- APIs
- JSON
- REST APIs
- Machine Learning fundamentals
- Large Language Models (LLMs)

---

# 🌟 Skills You Will Gain

By completing the repository, you will gain experience with:

- AI Agents
- Prompt Engineering
- Tool Calling
- Function Calling
- Structured Outputs
- Retrieval-Augmented Generation (RAG)
- AI Memory
- Multi-Agent Systems
- Workflow Automation
- Python Programming
- LLM APIs
- FastAPI Development

---

# 🎓 Recommended Learning Resources

### Official Repository

https://github.com/https-deeplearning-ai/agentic-ai-public

### DeepLearning.AI

https://www.deeplearning.ai/

### OpenAI Documentation

https://platform.openai.com/docs

### Anthropic Documentation

https://docs.anthropic.com/

### Google AI

https://ai.google/

### Hugging Face

https://huggingface.co/

### LangChain

https://python.langchain.com/

### LlamaIndex

https://docs.llamaindex.ai/

---

# 📄 License

Please refer to the original GitHub repository for the latest license information and usage terms:

https://github.com/https-deeplearning-ai/agentic-ai-public

---

# 🙏 Acknowledgements

This repository is maintained by **DeepLearning.AI** and provides educational resources for learning modern **Agentic AI** concepts through practical examples and hands-on coding exercises.