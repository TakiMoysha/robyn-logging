FROM python:3.11-bookworm

WORKDIR /workspace

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /workspace

EXPOSE 8080

CMD ["python3", "main.py", "--log-level=WARN"]
