
# Logistic API

Logistic API is a Python-based application designed to manage and streamline logistics operations.

## Features

- **Order Management**: Create, update, and track orders efficiently.
- **Integration**: Easily integrates with other services via RESTful endpoints.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: The application is built using Python; download it from the [official website](https://www.python.org/downloads/).
- **Docker**: For containerization; install it from the [Docker website](https://www.docker.com/get-started).
- **Docker Compose**: To manage multi-container Docker applications; follow the installation guide [here](https://docs.docker.com/compose/install/).

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/gominibui/logistic_api.git
   cd logistic_api
   ```

2. **Set Up Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

2. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at `http://127.0.0.1:8000/`.

## Docker Deployment

1. **Build and Start Containers**:

   ```bash
   docker-compose up --build
   ```

2. **Access the API**:

   Once the containers are up and running, the API will be available at `http://localhost:8000/`.


## Contact

For any inquiries or issues, please open an issue in the repository or contact the maintainer at [your-email@example.com].
