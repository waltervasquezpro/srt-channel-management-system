
# SRT Channel Management System

A web-based application built with Python and Django to manage broadcast channel delivery configurations, customer records, and streaming services.

## Overview

SRT Channel Management System was developed to simplify the management of broadcast delivery services.

The application provides a centralized interface for organizing customers, television channels, delivery protocols, IP addresses, ports, and service statuses.

The project was developed and deployed on Linux, demonstrating practical experience in backend development, relational databases, web application design, and application deployment.

## Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap, JavaScript, AJAX |
| Database | SQLite (local development), PostgreSQL (original deployment) |
| ORM | Django ORM |
| Operating System | Windows (development), Ubuntu Linux (deployment) |
| Application Server | Gunicorn (original deployment) |

## Features

- Create, view, edit, and manage broadcast delivery services.
- Register and manage customers and television channels.
- Store delivery configurations, including protocols, IP addresses, and ports.
- Manage SRT Caller and Listener configuration records.
- Search and filter services by status.
- Track Active, Test, and Removed services.
- Authenticate users through Django's authentication system.
- Create customers and channels dynamically using AJAX-powered forms.

## Architecture

The application follows Django's Model-View-Template (MVT) architecture.

- **Frontend:** Django templates, Bootstrap, and JavaScript provide the user interface.
- **Backend:** Django handles HTTP requests, form validation, authentication, and business logic.
- **Database:** Django ORM manages relational data for customers, channels, and services.
- **Deployment:** The original application was deployed on an Ubuntu Linux server.

## Installation

### Prerequisites

- Python 3.12 or later
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/waltervasquezpro/srt-channel-management-system.git
cd srt-channel-management-system
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```cmd
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Generate a unique Django secret key:

```bash
python -c "from secrets import token_urlsafe; print(token_urlsafe(50))"
```

On Windows Command Prompt:

```cmd
set DJANGO_SECRET_KEY=YOUR_GENERATED_SECRET_KEY
set DJANGO_DEBUG=True
```

On macOS or Linux:

```bash
export DJANGO_SECRET_KEY="YOUR_GENERATED_SECRET_KEY"
export DJANGO_DEBUG=True
```

Replace `YOUR_GENERATED_SECRET_KEY` with the generated value.

### 5. Initialize the database

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Start the application

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

Log in using the administrator account created in the previous step.

## Project Scope

The application manages broadcast delivery configuration records. It does not directly provision SRT streams or provide real-time stream monitoring.

The public repository uses SQLite for local execution. The original deployment used PostgreSQL.

## Author

**Walter Vasquez**

