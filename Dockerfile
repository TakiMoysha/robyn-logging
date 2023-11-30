FROM python:3.11-bookworm

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 8080

CMD ["python3", "main.py", "--log-level=WARN"]
