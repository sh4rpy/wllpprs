FROM python:3.9

WORKDIR /code
COPY . .
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
