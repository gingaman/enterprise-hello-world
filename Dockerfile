# syntax=docker/dockerfile:1.7

# =============================================================================
#  HelloWorld™ container image
#  Multi-stage, non-root, distroless-adjacent, SBOM-friendly
# =============================================================================

# ---- Build stage -----------------------------------------------------------
FROM python:3.12-slim-bookworm AS builder

WORKDIR /build

RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md ./
COPY helloworld ./helloworld

RUN pip install --no-cache-dir --upgrade pip build && \
    python -m build --wheel

# ---- Runtime stage ---------------------------------------------------------
FROM python:3.12-slim-bookworm AS runtime

LABEL org.opencontainers.image.title="HelloWorld"
LABEL org.opencontainers.image.description="Cloud-native greeting orchestration platform"
LABEL org.opencontainers.image.version="2.0.0-rc.3"
LABEL org.opencontainers.image.vendor="HelloWorld Platform Team"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.source="https://git.example.com/platform/helloworld"

RUN groupadd --system --gid 1000 helloworld && \
    useradd --system --uid 1000 --gid helloworld --no-create-home helloworld

WORKDIR /app

COPY --from=builder /build/dist/*.whl /tmp/
RUN pip install --no-cache-dir /tmp/*.whl && rm -rf /tmp/*.whl

USER helloworld

EXPOSE 8080 9090

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8080/healthz')" || exit 1

ENTRYPOINT ["helloworld"]
