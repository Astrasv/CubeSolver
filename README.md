# Rubik's Cube Solver

## Overview

A Rubik's Cube solver with a FastAPI backend supporting 2x2 and 3x3 cubes with multiple solving algorithms (IDDFS, IDA\*, BFS).

## API Endpoints

| Method | Path            | Description                    |
| ------ | --------------- | ------------------------------ |
| POST   | `/solve/3x3`    | Solve a 3x3 Rubik's Cube       |
| POST   | `/solve/2x2`    | Solve a 2x2 Rubik's Cube       |

Refer to the API Docs in `http://localhost:8000/docs` after installation.


## Tech Stack

- **Python 3.14+**
- **FastAPI** - Web framework
- **uv** - Python package manager

## Setup the API server
### With docker

```bash
git clone https://github.com/Astrasv/CubeSolver.git
cd CubeSolver
docker compose up --build
```

The API will be available at `http://localhost:8000`.

### Without docker
#### 1. Install uv

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 2. Clone and sync dependencies

```bash
git clone https://github.com/Astrasv/CubeSolver.git
cd CubeSolver
uv sync
```

#### 3. Run the API

```bash
uv run fastapi dev app/main.py
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for the interactive Swagger documentation.


## Run with streamlit
If you want to quickly fiddle around with the logics, use `uv run streamlit_webpage.py` command to launch a streamlit webpage