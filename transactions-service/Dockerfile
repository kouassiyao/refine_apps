FROM python:3.12

WORKDIR /code/

# Install Poetry
RUN pip install poetry

# Install dependencies
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false && poetry install --only main

# Copy the rest of the application code
COPY ./app /code/app

ENV API_HOST=0.0.0.0
ENV API_PORT=8000

CMD ["sh", "-c", "uvicorn app.main:app --host ${API_HOST} --port ${API_PORT}"]
