FROM python:3.9-alpine
WORKDIR /code
ADD requirments.txt .
RUN pip install -r requirments.txt
COPY ./app /code/app

CMD  ["gunicorn", "-w 4", "app.main:app", "--bind", "0.0.0.0:8080"]