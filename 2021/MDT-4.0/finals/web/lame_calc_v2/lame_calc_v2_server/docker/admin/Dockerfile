FROM python:3.8

EXPOSE 5000

ENV FLASK_APP main.py
ENV FLASK_DEBUG 0

RUN groupadd -g 444 nobodi
RUN useradd -r -u 444 -g nobodi -m nobodi

RUN apt-get update -y
RUN pip install flask

COPY docker/admin/main.py /home/nobodi/main.py
COPY private/admin_secret.txt /home/nobodi/f4pl1bvsqQ.txt
COPY private/flag.txt /flag_for_you.txt

WORKDIR /home/nobodi
USER nobodi

CMD flask run --host 0.0.0.0