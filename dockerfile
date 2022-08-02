FROM python:3.9.0

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /home/sns

WORKDIR /home/sns

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /home/sns
