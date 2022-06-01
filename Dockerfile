FROM python:3.10-slim

LABEL maintainer="Sergio Rivera <sriveralopez50@gmail.com>""

RUN pip install pyftpdlib

WORKDIR /ftp

RUN mkdir -p file-servers/auth-fs file-servers/anon-fs

COPY server.py .

EXPOSE 21 30000-30009

CMD [ "python", "./server.py" ]
