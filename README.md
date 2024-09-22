# 🥊 UFC Fight App: No Spoilers!

A web application that displays past and upcoming UFC fights without spoiling the results for users who want to watch past events at their own pace. The app ensures that you can view the schedule in chronological order without accidentally seeing the results of previous fights.

This project is containerized using Docker and Docker Compose for easy deployment and management of both the frontend and backend.

## 🚀 Features

- **No Spoilers**: Past fights are hidden from view by default, so you can avoid spoilers and watch fights in sequence.
- **Upcoming Fights**: Check the schedule of all upcoming UFC events.
- **Past Fights**: View the list of previous events and reveal the fight results only when you're ready.
- **Fight Details**: Each fight card includes key details about the fighters and the event.
- **Scraper-Driven Database**: Data is dynamically fetched and populated into a SQLite database using a custom web scraper.

## 🛠️ Tech Stack

- **Frontend**: Plain JavaScript, HTML, and CSS.
- **Backend**: Python Flask for serving API requests and managing the database.
- **Database**: SQLite for storing fight data.
- **Scraper**: A custom Python-based scraper used to populate the database with UFC event data.
- **Containerization**: Docker and Docker Compose for managing and deploying the app across different environments.

## 🐳 Dockerized Setup

This project leverages Docker containers for easy deployment. Using Docker Compose, both the frontend (JavaScript) and the backend (Flask with SQLite) are deployed as separate services.

