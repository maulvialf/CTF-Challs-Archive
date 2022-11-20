FROM python:3-alpine

COPY flag.txt /REDACTED
COPY src /opt/calculator

WORKDIR /opt/calculator
RUN pip install -r requirements.txt

USER nobody

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
