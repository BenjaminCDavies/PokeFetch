
FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /pokefetch

# Configure uv for container-friendly dependency installation
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy dependency metadata first for better build caching
COPY pyproject.toml uv.lock ./

# Install dependencies without installing the project itself yet
RUN uv sync --frozen --no-install-project

# Copy application source
COPY src ./src

# Install the project
RUN uv sync --frozen

# Make the virtual environment available on PATH
ENV PATH="/pokefetch/.venv/bin:$PATH"

EXPOSE 8000

CMD ["fastapi", "run", "src/pokefetch/main.py", "--host", "0.0.0.0", "--port", "8000"]
