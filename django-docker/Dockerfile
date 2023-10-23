FROM python:3.9-alpine
WORKDIR /code
ADD requirments.txt .
RUN pip install -r requirments.txt
ADD manage.py .
COPY ./django_project /code/django_project

RUN python3 manage.py migrate
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "3", "django_project.wsgi:application"]