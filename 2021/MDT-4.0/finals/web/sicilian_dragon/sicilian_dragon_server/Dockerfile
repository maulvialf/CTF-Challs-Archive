FROM python:3.8.4

EXPOSE 20001

ENV FLASK_APP main.py
ENV FLASK_DEBUG 0

RUN groupadd -g 444 nobodi
RUN useradd -r -u 444 -g nobodi -m nobodi

#RUN apt-get update -y
RUN pip install flask

COPY fetch_app /home/nobodi/fetch_app

WORKDIR /home/nobodi/fetch_app
USER nobodi

CMD flask run --host 0.0.0.0 --port 20001
