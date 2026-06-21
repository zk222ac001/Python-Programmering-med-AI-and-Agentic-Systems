# Reflective Research Agent

*Source: GitHub – https-deeplearning-ai/agentic-ai-public*
*URL: https://github.com/https-deeplearning-ai/agentic-ai-public*

## Overview

**Reflective Research Agent** is a FastAPI-based web application that plans and runs a research workflow using multiple AI agents.

The application can:

* Plan a research workflow
* Run tool-using agents
* Use Tavily, arXiv, and Wikipedia as research tools
* Store task state and results in PostgreSQL
* Run locally using Docker

## Purpose

This repository provides a **Research Agent service** for the **Agentic Workflow course**.

The system follows a multi-step agent workflow:

1. Planner agent creates a research plan
2. Research agent gathers information
3. Writer agent produces the report
4. Editor agent improves the final output

## Main Features

* `/` serves a simple UI for starting a research task
* `/generate_report` starts a threaded multi-step agent workflow
* `/task_progress/{task_id}` shows live progress for each step
* `/task_status/{task_id}` returns final task status and report

## Project Structure

```text
.
├─ main.py
├─ src/
│  ├─ planning_agent.py
│  ├─ agents.py
│  └─ research_tools.py
├─ templates/
│  └─ index.html
├─ static/
├─ docker/
│  └─ entrypoint.sh
├─ requirements.txt
├─ Dockerfile
└─ README.md
```

## Key Components

### `main.py`

Contains the FastAPI application.

### `src/planning_agent.py`

Contains planner-related logic, including:

* `planner_agent()`
* `executor_agent_step()`

### `src/agents.py`

Contains agent implementations such as:

* Research agent
* Writer agent
* Editor agent

### `src/research_tools.py`

Contains external research tools:

* Tavily search tool
* arXiv search tool
* Wikipedia search tool

### `templates/index.html`

Provides the UI page rendered at `/`.

### `docker/entrypoint.sh`

Starts PostgreSQL, prepares the database, and launches Uvicorn.

## Prerequisites

You need:

* Docker
* OpenAI API key
* Tavily API key

Create a `.env` file:

```env
OPENAI_API_KEY=your-open-api-key
TAVILY_API_KEY=your-tavily-api-key
```

## Environment Variables

The app uses `DATABASE_URL` at startup.

Default local development database URL:

```text
postgresql://app:local@127.0.0.1:5432/appdb
```

Optional PostgreSQL variables:

```env
POSTGRES_USER=app
POSTGRES_PASSWORD=local
POSTGRES_DB=appdb
```

## Build and Run

### 1. Build the Docker Image

```bash
docker build -t fastapi-postgres-service .
```

### 2. Run the Container

```bash
docker run --rm -it \
  -p 8000:8000 \
  -p 5432:5432 \
  --name fpsvc \
  --env-file .env \
  fastapi-postgres-service
```

### 3. Open the App

UI:

```text
http://localhost:8000/
```

API docs:

```text
http://localhost:8000/docs
```

## API Quickstart

### Start a Research Task

```bash
curl -X POST http://localhost:8000/generate_report \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Large Language Models for scientific discovery", "model":"openai:gpt-4o"}'
```

Response:

```json
{
  "task_id": "UUID..."
}
```

### Check Task Progress

```bash
curl http://localhost:8000/task_progress/<TASK_ID>
```

### Get Final Report

```bash
curl http://localhost:8000/task_status/<TASK_ID>
```

## Troubleshooting

### UI Does Not Load

Check that `templates/index.html` exists inside the container:

```bash
docker exec -it fpsvc bash -lc "ls -l /app/templates && ls -l /app/static || true"
```

Watch logs:

```bash
docker logs -f fpsvc
```

### Database URL Error

Make sure the database URL is valid:

```text
postgresql://<user>:<password>@<host>:<port>/<database>
```

### Tables Disappear on Restart

The app may call:

```python
Base.metadata.drop_all(bind=engine)
```

Guard it with an environment flag:

```python
if os.getenv("RESET_DB_ON_STARTUP") == "1":
    Base.metadata.drop_all(bind=engine)
```

### Tavily, arXiv, or Wikipedia Errors

Make sure your `.env` file contains:

```env
OPENAI_API_KEY=your-open-api-key
TAVILY_API_KEY=your-tavily-api-key
```

Also confirm that the container has network access.

## Development Tips

### Run with Hot Reload

```bash
docker run --rm -it \
  -p 8000:8000 \
  -p 5432:5432 \
  -v "$PWD":/app \
  --name fpsvc fastapi-postgres-service \
  bash -lc "pg_ctlcluster \$(psql -V | awk '{print \$3}' | cut -d. -f1) main start && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
```

### Connect to PostgreSQL

```bash
psql "postgresql://app:local@localhost:5432/appdb"
```

## Technologies Used

* Python
* FastAPI
* PostgreSQL
* Docker
* Uvicorn
* SQLAlchemy
* Jinja2
* Tavily
* arXiv
* Wikipedia
* OpenAI-compatible model usage

## Summary

This project is a local development service for building and running a reflective research agent. It combines a FastAPI web interface, PostgreSQL task storage, Docker-based deployment, and multiple research tools to create structured research reports through an agentic workflow.
