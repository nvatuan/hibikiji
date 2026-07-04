FROM --platform=linux/arm64 python:3.10 

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FAIL_WITH_REDIS=false \
  REDIS_HOST=localhost \
  REDIS_PORT=6379 \
  HOST=localhost \
  PORT=5071

CMD ["python", "main.py"]
