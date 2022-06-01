FROM python:3.10-slim

LABEL maintainer="Sergio Rivera <sriveralopez50@gmail.com>"

WORKDIR /ftp
COPY *.py requirements.txt ./
RUN mkdir file-servers
RUN pip install -r requirements.txt

EXPOSE 21 30000-30009

CMD [ "python", "./ftpd.py" ]
