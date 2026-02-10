# Enterprise AI Job Platform – Skill Extraction API

A production-style AI backend built with **FastAPI**, **Docker**, and **NLP**, designed to extract technical skills from free-text job descriptions or resumes.

This project demonstrates how modern AI systems expose intelligence via REST APIs and are deployed in containerized environments.
---

## 🚀 Features

- REST API built with FastAPI
- Real AI logic for skill extraction from text
- Dockerized backend (production-ready)
- Clean, scalable project structure
- Linux / WSL compatible
- Ready for future upgrades (LLMs, RAG, Vector DBs, Spark)
---

## 🛠 Tech Stack

- Python 3.10
- FastAPI
- Pydantic
- Docker
- Uvicorn
- NLP (rule-based skill extraction)
- Linux / WSL
---

## 📂 Project Structure

enterprise-ai-job-platform/
├── api/
│   └── main.py              # FastAPI application
├── ai/
│   ├── skill_extractor.py   # Skill extraction logic
│   ├── model.py             # Reserved for future ML models
│   └── __init__.py
├── data/                    # Sample / future datasets
├── spark/                   # Reserved for Spark pipelines
├── docker/                  # Docker-related configs
├── Dockerfile
├── requirements.txt
└── README.md

