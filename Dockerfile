FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir poetry \
    && poetry install --no-root

RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN poetry add whitenoise

RUN poetry run python manage.py collectstatic --noinput --clear \
    && chmod -R 755 /app/static \
    && chown -R www-data:www-data /app/static
