# 🚆 RailSathi - Passenger Complaint API

This project is a backend service built using Django and Docker. It allows passengers to submit complaints which are saved to a PostgreSQL database and also emailed to the support team. The project is containerized with Docker and uses environment variables for configuration.

##  Features

- Submit passenger complaints via API
- Store complaint data in PostgreSQL
- Email notification sent using templated content
- Dockerized setup with Docker Compose
- Environment variables managed via `.env` file

## Technologies

- Python 3.10
- Django 5.2.4
- Django REST Framework
- PostgreSQL 15
- Docker & Docker Compose
- Gmail SMTP for email delivery

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd railsathi_project
```

### 2. Configure Environment

Copy `.env.example` to `.env` and fill in your values:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1

POSTGRES_DB=railsathi
POSTGRES_USER=railsathi_user
POSTGRES_PASSWORD=railsathi_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
DEFAULT_FROM_EMAIL=your_email@gmail.com
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### 3. Build and Run with Docker

```bash
docker-compose up --build
```

API available at: [http://localhost:8000/items/submit-complaint/](http://localhost:8000/items/submit-complaint/)

##  API Endpoint

### POST `/items/submit-complaint/`

Accepts complaint data in JSON format and sends an email using the templated message.

#### Sample Request Body:

```json
{
  "passenger_name": "Amit",
  "user_phone_number": "9876543210",
  "train_no": "12345",
  "train_name": "Rajdhani Express",
  "start_date_of_journey": "2025-07-14",
  "coach": "B1",
  "berth": "12",
  "pnr": "1234567890",
  "description": "AC not working in coach",
  "train_depo": "Delhi"
}
```

##  Design Decisions & Assumptions

- Email is sent in plain text format using Django's `send_mail` and `render_to_string`.
- Templated email is stored at `templates/email/complaint_email.txt`.
- Admin panel is enabled, and model is registered for manual viewing (optional).
- REST Framework is used for easy API extension.

##  Testing

- Use Postman or curl to test the API.
- Check your inbox to confirm that the email is sent correctly.
- Logs will show if the complaint was saved or if email failed.

##  Project Structure Overview

```
railsathi/
├── items/
│   ├── migrations/
│   ├── templates/email/complaint_email.txt
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── railsathi/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── entrypoint.sh
├── .env
```

