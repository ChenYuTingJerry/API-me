FROM python:3.8-slim

COPY . /app
WORKDIR /app

EXPOSE 8000
RUN pip install -r requirements.txt

ENTRYPOINT ["python","main.py"]