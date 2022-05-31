FROM python:2.7

RUN pip install pyftpdlib

WORKDIR /ftp

COPY server.py .

EXPOSE 21

CMD [ "python", "./server.py" ]
