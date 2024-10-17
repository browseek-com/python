FROM python:3.12

WORKDIR /app

COPY src/ src/
COPY examples/ examples/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install && \
    playwright install-deps && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/pip

# Set default environment variables
ENV MAX_CONCURRENT_BROWSERS=5 \
    DEFAULT_TIMEOUT=30 \
    RETRY_ATTEMPTS=3 \
    PROXY_ENABLED=True \
    PROXY_ROTATE_ON_FAILURE=True \
    DNS_OVER_HTTPS=True \
    CAPTCHA_SERVICE=2captcha

CMD ["python", "examples/docker_example.py"]
