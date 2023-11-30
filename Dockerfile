FROM python:3.11-bookworm

ENV POETRY_VERSION=1.6.1 \
  POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN ls -l .
RUN ls -l /app


RUN pip install "poetry==$POETRY_VERSION"

COPY . /app/
RUN ls -l /app

RUN poetry install $(test "$YOUR_ENV" == production && echo "--no-dev")

EXPOSE 8080

CMD ["python3", "main.py", "--log-level=WARN"]
