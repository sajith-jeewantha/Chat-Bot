# 🧠 TF-IDF Chat Bot — Dockerized Retrieval Chatbot

A lightweight retrieval-based chatbot powered by **TF-IDF vectorization** and **cosine similarity search**.  
Instead of generating responses, the bot finds the most relevant answer from a prepared dataset of conversation pairs.

Designed for fast deployment, low resource usage, and domain-specific chatbot use cases.

---

## 🚀 Features

- TF-IDF vector search engine
- Cosine similarity ranking
- Retrieval-based responses
- Deterministic answers
- Confidence threshold fallback
- Lightweight CPU runtime
- No large language model required
- Docker ready
- JSONL dataset support

---

## ⚙️ How It Works

1. Loads conversation pairs from `pairs.jsonl`
2. Builds TF-IDF vector index on startup
3. Converts each user message into a vector
4. Computes cosine similarity vs stored inputs
5. Returns the best matching response
6. Uses a similarity threshold to avoid weak matches

If confidence is low, the bot returns a safe fallback reply.

## Run with Docker
### Pull Image
```bash
docker pull sajithjeewantha/chat-bot:v1.0
```

### Run Container
```bash
docker run --name chat-bot-live -p 5001:5000 sajithjeewantha/chat-bot:v1.0
```

## 🐳 Docker Hub

Image available on Docker Hub:

👉 [sajithjeewantha/chat-bot](https://hub.docker.com/r/sajithjeewantha/chat-bot)


## 📦 Dataset Format

Dataset file:

Format (JSONL — one JSON object per line):

```json
{"input":"Hello","output":"Hi there!"}
{"input":"What is AI?","output":"Artificial Intelligence is..."}
```

## 🗂 Project Structure
```css
.
├── src/
│   ├── pairs.jsonl
│   ├── bot.py
│   └── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```
---

## 🙏 Thank You

Thanks for visiting this repository and trying the chatbot project.  
Your feedback and suggestions are always welcome.

If this project helped you, please consider ⭐ starring the repo.

---

- 💼 LinkedIn: [Connect on LinkedIn](https://www.linkedin.com/in/sajith-jeewantha)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


