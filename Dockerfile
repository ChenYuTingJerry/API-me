FROM python:3.8-slim

COPY ./app /project/app
WORKDIR /project
COPY ./config ./config
ADD ./requirements.txt ./
ADD ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./run.py ./run.py
RUN chmod +x ./run.py

EXPOSE 3000
RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
