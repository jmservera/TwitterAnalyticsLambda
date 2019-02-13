FROM python:3.7.2-stretch

COPY /TweetIngest/requirements.txt /ingest/
RUN pip install -r /ingest/requirements.txt

COPY /TweetIngest/. /ingest/

CMD python /ingest/main.py


