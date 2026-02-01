FROM python:3.7-alpine

WORKDIR /backend-api

COPY ./requirements.txt /backend-api
RUN pip install -r requirements.txt

COPY . /backend-api

CMD ["python", "app.py"]