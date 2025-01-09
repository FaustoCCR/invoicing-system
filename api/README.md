# Invoicing API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-orange)

## Overview

Invoicing API is designed to handle billing and accounting functionalities, providing endpoints for managing invoices, inventory, products, users, etc. This API serves as the backend for applications that require reliable billing and inventory solutions.

## Features

- Create, read, update, and delete invoices
- Manage customer accounts
- Track inventory

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: For database interactions.
- **JWT**: For secure authentication.
- **Docker**: For containerization.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10 or higher
- Docker (if you plan to run the application in a container)

### Set up project

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Environment Variables

This application requires several environment variables to be set for proper configuration:

- `APP_NAME`: The name of your application.
- `SECRET_KEY`: A secret key for session management.
- `JWT_SECRET_KEY`: A secret key for JWT authentication.
- `DATABASE_URI`: The URI for your database connection.

You can set these variables in your terminal or create a `.env` file in your project.

### Running the Application

```bash
flask run
```

#### Using Docker

To build and run the application using Docker, execute the following commands:

1. Build the Docker image:

```bash
docker build -t invoicing-api .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 --env-file .env invoicing-api
```

### Accessing the API

Once the application is running, you can access the API at: http://localhost:5000.

For detailed API documentation, you can access the Swagger UI at: http://localhost:5000/docs
