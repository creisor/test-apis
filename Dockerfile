FROM python:3-alpine as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY app.py /app/app.py

WORKDIR /app

ENV FLASK_APP app

ENV PORT ${PORT}

CMD ["flask", "run", "--host=0.0.0.0"]
