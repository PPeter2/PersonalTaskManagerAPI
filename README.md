# 📝 Personal Task Manager API

## ⚠️ Introduction
This project was built from scratch to learn backend development with Python.
It is a simple REST API that lets you create, read, update and delete tasks.

## 🎯 What I Learned
1. Python 3
2. FastAPI — building REST APIs
3. PostgreSQL — relational database
4. SQLAlchemy — talking to the database with Python
5. Alembic — database migrations
6. pytest — writing and running tests
7. Docker — containerizing services
8. Docker Compose — running multiple services together
9. uv — modern Python package manager

## 🛠️ File Structure
```
PersonalTaskManagerAPI/
│
├── app/
│   ├── init.py
│   ├── main.py              ← FastAPI app entry point
│   ├── database.py          ← database connection
│   ├── models/
│   │   └── task.py          ← database table definition
│   ├── schemas/
│   │   └── task.py          ← data validation
│   ├── services/
│   │   └── task_service.py  ← business logic
│   └── api/
│       └── tasks.py         ← API endpoints
│
├── tests/
│   ├── test_tasks.py        ← all tests
│   └── conftest.py          ← test setup
│
├── .env                     ← your secrets (not pushed to git)
├── .env.example             ← template for others
├── .gitignore
├── docker-compose.yml       ← runs PostgreSQL in Docker
├── Dockerfile               ← builds the app container
├── pyproject.toml           ← dependencies
└── README.md
```

## ⚙️ Tech Stack

```
Language:    Python 3.13
Framework:   FastAPI
Database:    PostgreSQL 15
ORM:         SQLAlchemy
Migrations:  Alembic
Testing:     pytest
Container:   Docker + Docker Compose
Packages:    uv
```

## 🚀 How To Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/PersonalTaskManagerAPI.git
cd PersonalTaskManagerAPI
```

### 2. Create your .env file
```bash
cp .env.example .env
```

### 3. Start the database
```bash
docker-compose up -d
```

### 4. Start the app
```bash
uv run uvicorn app.main:app --reload
```

### 5. Open in browser
```
http://localhost:8000/docs
```

## 🧪 Running Tests
```bash
uv run pytest tests/ -v
```

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get one task |
| POST | /tasks | Create a task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |
| GET | /health | Health check |
