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

CMD ["python", "examples/docker_example.py"]
