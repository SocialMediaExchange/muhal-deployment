FROM python:3.8

RUN apt-get update && apt-get install -y gettext

RUN mkdir /home/muhal-backend
ADD https://api.github.com/repos/SocialMediaExchange/muhal-backend/tarball/ /home/muhal-backend.tar.gz
RUN tar -xvzf /home/muhal-backend.tar.gz -C /home/muhal-backend --strip-components 1

WORKDIR /home/muhal-backend
RUN pip install -r requirements.txt
RUN pip install gunicorn 

WORKDIR /home/muhal-backend/muhal
COPY config/local_settings.py muhal/local_settings.py 
COPY ./start.sh .
RUN chmod +x start.sh