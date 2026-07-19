# Car Price Tracker

A data engineering project that continuously collects used car listings, processes them through a streaming pipeline, and stores them in a PostgreSQL database for analytics and price tracking.

---

# Motivation

I was looking to buy a second-hand car.

Websites like CarDekho contain thousands of listings, but visiting the website every day to check whether the price of a particular car has dropped quickly becomes repetitive.

Instead, I wanted a system that could automatically monitor listings, store historical data, and eventually notify me whenever something interesting happens.

Examples include:

- A car's price drops
- A new listing matching my criteria appears
- A listing is removed
- A dealer updates an existing listing

This project automates that workflow.

Currently, the pipeline collects listing data from CarDekho and stores it in PostgreSQL through a Kafka-based streaming architecture.

Once sufficient historical data has been collected, SQL queries can be used to generate reports and eventually send email alerts.

---

# Architecture

<p align="center">
    <img src="docs/architecture.png" width="900">
</p>

## Data Flow

```
CarDekho
    │
    ▼
 Web Scraper
    │
    ▼
Kafka Producer
    │
    ▼
 Kafka Topic
    │
    ▼
Kafka Consumer
    │
    ▼
    ETL
    │
    ▼
 FastAPI
    │
    ▼
PostgreSQL
```

---

# Current Features

- FastAPI REST API
- PostgreSQL database
- SQLAlchemy ORM
- Pydantic request validation
- Dockerized API and database
- Playwright web scraper
- Kafka Producer
- Kafka Consumer
- ETL pipeline
- Automatic data persistence

---

# Project Progress

## Phase 1 — FastAPI

Completed

- FastAPI setup
- Basic API
- GET endpoints
- POST endpoints
- OpenAPI documentation
- Swagger UI exploration

---

## Phase 2 — Database

Completed

- PostgreSQL installation
- SQLAlchemy integration
- Environment configuration using `.env`
- Database connection
- Car ORM model
- Automatic table creation
- CRUD endpoints
- Pydantic validation
- Improved project structure

---

## Phase 3 — Containerization

Completed

- Dockerfile
- Docker Compose
- PostgreSQL container
- API container

---

## Phase 4 — Scraper

Completed

- Playwright scraper
- BMW listing extraction
- Updated database schema
- Updated API models
- Listing parsing

---

## Phase 5 — Streaming Pipeline

Completed

- Kafka Producer
- Kafka Consumer
- ETL layer
- Consumer posts processed data to FastAPI
- FastAPI stores processed data into PostgreSQL

---

# Roadmap

## In Progress

- Support more brands
- Improve scraper resiliency
- Better duplicate detection

## Planned

- Incremental updates instead of full scraping
- Detect price changes
- Detect removed listings
- Historical price tracking
- Scheduled SQL reports
- Email notifications
- Dashboard for analytics
- Deployment

---

# Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Kafka
- Docker
- Playwright
- Pydantic

---

# Repository Structure

```
.
├── app/
│   ├── api/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── scraper/
│
├── producer/
│
├── consumer/
│
├── docker/
│
├── docs/
│   └── architecture.png
│
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# Getting Started

## 1. Create a virtual environment

```bash
python -m venv .venv

# Bash
source .venv/bin/activate

# Fish
source .venv/bin/activate.fish
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Install PostgreSQL

Arch Linux

```bash
sudo pacman -S postgresql

psql --version

sudo -iu postgres initdb -D /var/lib/postgres/data

sudo systemctl enable postgresql
sudo systemctl start postgresql
```

Optional

```bash
sudo pacman -S dbeaver
```

---

## 3. Install Docker

```bash
sudo pacman -S docker

docker --version

docker compose --version

docker run hello-world
```

---

## 4. Install Playwright

```bash
pip install playwright

playwright install
```

---

# Development Notes

Freeze dependency versions once the project is stable.

```bash
pip freeze > requirements-lock.txt
```

---

# Future Improvements

- Historical price visualization
- Scheduled scraping
- Multiple data sources
- Async scraping workers
- Better ETL validation
- Airflow orchestration
- CI/CD pipeline
- Cloud deployment
- Prometheus metrics
- Grafana dashboards

---

# Current Status

The end-to-end ingestion pipeline is complete.

```
Scraper
    ↓
Kafka Producer
    ↓
Kafka Topic
    ↓
Kafka Consumer
    ↓
ETL
    ↓
FastAPI
    ↓
PostgreSQL
```

The next milestone is building the analytics layer that periodically runs SQL queries on historical data and sends email notifications whenever a listing satisfies predefined conditions such as price drops or newly matching vehicles.
