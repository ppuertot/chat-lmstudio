# Local AI Chat Interface

A lightweight web chat powered by a **local LM Studio** model (default: `openai/gpt-oss‑20b`).

---
## 📦 Project structure
```
workspace/
├── app.py
├── Dockerfile
├── README.md
├── docker-compose.yml          # host network (recommended for single container)
├── docker-compose-bridge.yml   # bridge network, maps port 8000
├── requirements.txt
└── static/                     # web UI files
    ├── index.html
    └── chat.js
```
---
## ⚙️ Prerequisites
| Item | Version |
|------|---------|
| Python | ≥ 3.11 |
| Docker (20+) | – |
| LM Studio | Running locally on port **1234** (default) |

> The chat app expects the LM Studio HTTP API to be reachable at `http://localhost:1234` (or a URL you set via `LMSTUDIO_URL`).
---
## 🚀 Local development (Python)
```bash
# Create virtual env and activate
python -m venv .venv && source .venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run the server
uvicorn app:app --reload
```
Open <http://localhost:8000>.
---
## 📦 Docker Compose – **host network** (recommended)
```bash
docker compose up --build        # uses docker-compose.yml
```
The container shares the host’s networking stack, so `localhost` inside it points to your machine. The app will automatically use `http://localhost:1234`.
---
## 📦 Docker Compose – **bridge network** (port mapping)
```bash
docker compose -f docker-compose-bridge.yml up --build
```
The service publishes port 8000 on the host and sets `LMSTUDIO_URL=http://host.docker.internal:1234`. The `extra_hosts` entry resolves `host.docker.internal` to the gateway IP.
---
## 🛠️ Configuring LM Studio for Docker bridge
If you use the bridge compose file, make sure LM Studio listens on **all interfaces**:
```bash
lmstudio --host 0.0.0.0      # or adjust its config accordingly
```
Otherwise the container will be unable to reach it.
---
## 🔧 Customizing the model
Edit `app.py` and change `LMSTUDIO_BASE` or the `model` field inside `get_local_model_response`. Example:
```python
# Use a different model ID
payload["model"] = "qwen/qwen3.5-9b"
```
---
## 🤝 Contributing
Pull requests are welcome! Please open an issue first if you plan on adding new features.
---
## 📄 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
