FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN uv sync --frozen --no-cache

# Run migrations and collect static files
RUN /app/.venv/bin/python manage.py migrate
RUN /app/.venv/bin/python manage.py collectstatic --noinput

# Run the application
CMD ["/app/.venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
