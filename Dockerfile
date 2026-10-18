FROM python:3.12-slim

# Print Python output immediately instead of buffering it,
# so `docker compose up` shows results live.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY benchmark.py .

# The ollama Python library reads OLLAMA_HOST from the environment,
# so the script itself needs no changes. docker-compose.yml sets it.
CMD ["python", "benchmark.py"]