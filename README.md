# Local AI Chat Interface

A lightweight web chat powered by a local LM Studio model.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

> **NOTE:** Replace the placeholder `get_local_model_response` in *app.py* with your actual LM Studio SDK call.

## Run
```bash
uvicorn app:app --reload
```
Open <http://localhost:8000> in a browser.
