# Stage 1: Build environment
FROM python:3.12-slim as build-env

ENV PYTHONUNBUFFERED=1

# Install dependencies required for building some of the Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY src/requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Stage 2: Runtime environment
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    procps \
    libmariadb3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Copy dependencies from build stage
COPY --from=build-env /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build-env /usr/local/bin /usr/local/bin

COPY src .

ENV ll="ls -lah"

RUN chmod +x entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
