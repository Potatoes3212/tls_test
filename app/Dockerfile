FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl build-essential netcat-openbsd \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


RUN curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="/root/.local/bin:$PATH" \
    && poetry config virtualenvs.create false

ENV PATH="/root/.local/bin:${PATH}"


WORKDIR /opt/app

COPY ./pyproject.toml  ./poetry.lock ./

COPY ./app .

RUN poetry install

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
