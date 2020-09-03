FROM python:3.8-slim


RUN apt-get update && apt-get install -y curl
RUN curl https://raw.githubusercontent.com/Droplr/aws-env/master/bin/aws-env-linux-amd64 --output /bin/aws-env && \
  chmod +x /bin/aws-env

COPY ./app /project/app
WORKDIR /project
COPY ./config ./config
ADD ./requirements.txt ./
ADD ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./run.py ./run.py
RUN chmod +x ./run.py

EXPOSE 3000
RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
