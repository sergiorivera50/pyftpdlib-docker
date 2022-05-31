#!/bin/bash
docker build -t pyftpdlib-docker .
docker run -it --rm -p 21:21 -v $(pwd)/file-servers:/ftp/file-servers pyftpdlib-docker
