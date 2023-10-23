FROM python:3.9-alpine
WORKDIR /code
ADD requirments.txt .
RUN pip install -r requirments.txt
COPY ./app /code/app
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]