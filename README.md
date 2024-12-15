# Flask-MySQL Website with Docker Compose 🚀

This project is a robust and scalable web application built with **Flask** as the backend framework and **MySQL** as the database, all seamlessly managed using **Docker Compose**. The project is designed for ease of deployment, flexibility, and extensibility, making it perfect for both development and production environments.

---

## Features 🌟

- **Flask Framework**: Lightweight and flexible for building web applications.
- **MySQL Database**: Reliable and powerful relational database management system.
- **Dockerized Setup**: Fully containerized using Docker and Docker Compose.
- **Persistent Database Storage**: Ensures data is not lost between container restarts.
- **User Authentication**: Includes a login system with admin privileges.
- **Volume Mounting**: Hot-reload support during development.
- **Environment Variables**: Secure and configurable settings.

---

## Project Structure 📂




---

## Prerequisites ⚙️

Ensure the following are installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Setup & Installation 🛠️

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/flask-mysql-docker.git
   cd flask-mysql-docker


---

## Usage 🚀

### Development

- Flask hot-reloading is enabled for development.
- Any changes to the codebase will automatically reflect when you refresh the browser.

### Database Management

- The MySQL database is initialized using the configurations in `.env`.
- Data is stored persistently in the `db_data/` directory.

---

## Docker Services 🐳

- **Backend**: Flask app running on port `5000`.
- **Database**: MySQL server running on port `3306`.

To bring up or down the services:

```bash
docker-compose up   # Start all services
docker-compose down # Stop all services
