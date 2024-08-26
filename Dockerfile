FROM python:3.10-slim

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install --upgrade pip && \
    pip install pipenv

COPY . /usr/src/app

RUN pipenv lock && \
    pipenv install --system --deploy

EXPOSE 8000

WORKDIR /usr/src/app/src

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "-t", "300", "main:app"]