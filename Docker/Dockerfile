FROM python:3.6.7-stretch

COPY /TweetIngest/requirements.txt /ingest/
RUN pip install -r /ingest/requirements.txt

COPY /TweetIngest/. /ingest/

EXPOSE 80

WORKDIR /ingest

CMD python main.py


