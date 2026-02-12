# Enterprise AI Job Platform

A production-ready, Dockerized FastAPI backend that extracts and structures skills from resumes using AI-based processing.  
Designed as a foundation for enterprise hiring platforms, ATS systems, and AI-driven job matching solutions.

---

## 🚀 What This Project Does

This service:
- Accepts resume text or documents
- Extracts structured skills using AI logic
- Exposes clean REST APIs for integration with job platforms
- Is fully containerized using Docker for production readiness

This project is built with **scalability, modularity, and enterprise use cases** in mind.

---

## 🧠 Why This Matters

Hiring platforms struggle with:
- Unstructured resume data
- Inconsistent skill formats
- Manual screening inefficiencies

This backend solves that by:
- Converting raw resume data → structured skill intelligence
- Enabling AI-powered job matching and analytics
- Acting as a core service in an enterprise AI hiring stack

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI
- **AI Layer:** Custom skill extraction logic (extensible to LLMs / embeddings)
- **API:** RESTful endpoints
- **Containerization:** Docker
- **Architecture:** Modular service-based design

---

## 📂 Project Structure

```text
enterprise-ai-job-platform/
│
├── api/              # FastAPI application and routes
├── ai/               # AI logic (skill extraction, models)
├── Dockerfile        # Docker configuration
├── requirements.txt  # Python dependencies
└── README.md
```

## 🌐 Live Demo

Production API deployed on Render:

Base URL:
https://enterprise-ai-job-platform.onrender.com

Swagger Documentation:
https://enterprise-ai-job-platform.onrender.com/docs

Example Endpoints:

POST /predict → Extract skills from resume text  
POST /match → Calculate skill match score between resume and job description


