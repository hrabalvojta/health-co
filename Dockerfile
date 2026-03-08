FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Application code + baseline governance policies.
COPY requirements.txt .
COPY src/ ./src/
COPY governance/policies/ ./policies/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run as non-root for safer on-prem deployments.
RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app
USER appuser

# Placeholder command until the API/service entrypoint is finalized.
CMD ["python", "src/agent.py"]
