FROM python:2.7-slim

# backend dependencies (uwsgi)
RUN apt-get update && apt-get install -y gcc && apt-get clean

COPY ./code/backend/setup /code/backend/setup
RUN pip install /code/backend/setup

COPY ./code /code

COPY docker-entrypoint.sh /docker-entrypoint.sh
WORKDIR /code/backend
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["uwsgi", "--http-socket", "0.0.0.0:5000", "--wsgi-file", "run.py", "--callable", "app", "--master", "--processes", "2", "--threads", "2"]
