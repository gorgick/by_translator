FROM python:3.8-alpine
COPY requirements.txt /temp/requirements.txt
COPY translator /translator
WORKDIR /translator
EXPOSE 8000
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password tran-user
USER tran-user

