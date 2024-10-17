FROM python:3.9

WORKDIR /app

COPY src/ src/
COPY examples/ examples/
COPY examples/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/pip


CMD ["python", "examples/docker_example.py"]
