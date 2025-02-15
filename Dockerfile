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

# Collect static files
RUN /app/.venv/bin/python manage.py collectstatic --noinput

# Create data directory for SQLite
RUN mkdir -p /app/data

# Run the application
CMD ["/app/.venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
