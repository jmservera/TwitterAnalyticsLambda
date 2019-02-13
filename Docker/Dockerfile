FROM python:3.6.7-stretch

COPY /TweetIngest/requirements.txt /ingest/
RUN pip install -r /ingest/requirements.txt

COPY /TweetIngest/. /ingest/

# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
        && apt-get install -y --no-install-recommends dialog \
        && apt-get update \
	&& apt-get install -y --no-install-recommends openssh-server \
	&& echo "$SSH_PASSWD" | chpasswd 

COPY /WebApp/sshd_config /etc/ssh/
COPY /WebApp/init.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/init.sh

EXPOSE 80 2222

ENTRYPOINT ["init.sh"]