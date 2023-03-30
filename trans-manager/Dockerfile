FROM python:3.9-slim-buster

ENV PYTHONUNBEFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential

RUN mkdir /srv/docker-server
ADD . /srv/docker-server
COPY pyproject.toml /srv/docker-server


WORKDIR /srv/docker-server
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN python3 -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN pip install gunicorn

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

