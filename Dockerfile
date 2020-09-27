FROM python:3.8.5

WORKDIR /code
COPY . .
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000