FROM python:3.8-slim

COPY . /app
WORKDIR /app

EXPOSE 3000
RUN pip install -r requirements.txt

ENTRYPOINT ["python","run.py"]