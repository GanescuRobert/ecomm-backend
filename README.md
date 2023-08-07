# FastAPI Project with Uvicorn

[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.1-blue)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.17.4-blue)](https://www.uvicorn.org/)

# Create virtual environment:
```
python -m venv venv
source venv/bin/activate
```

# Install the project dependencies:
```
pip install -r requirements.txt
```

# Run the FastAPI application:
```
uvicorn app.main:app --reload
```

# Run Flake8 and check for linting issues:
```
flake8
```

# Run Black and format your code:
```
black .
```

# Run the tests:
```
pytest
```

# Build the Docker Image:
```
docker build -t ecomm-backend .
```

# Run the Docker Container:
```
docker run -d -p 8000:8000 ecomm-backend
```

# Run the Docker compose:
```
docker-compose up --build
```