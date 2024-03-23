FROM python:3.8

RUN mkdir /app
WORKDIR /app

ENV FLASK_APP=__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY ./app .
# CMD ["flask", "--app", "app", "--debug", "run"]
