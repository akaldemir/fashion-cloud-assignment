FROM python:3.11.4-alpine3.17
LABEL maintainer="akaldemir"

ENV PYTHONUNBUFFERED 1
ENV PATH="/py/bin:$PATH"
ARG DEVENV=false

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    if [ $DEVENV = "true" ]; then pip install -r requirements.dev.txt; fi

COPY src /src
WORKDIR /src