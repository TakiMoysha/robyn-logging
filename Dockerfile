FROM python:3.11-bookworm

ENV POETRY_VERSION=1.6.1 \
  POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app
COPY . /app/

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry install $(test "$YOUR_ENV" == production && echo "--no-dev")

EXPOSE 8080

CMD ["python3", "main.py", "--log-level=WARN"]
