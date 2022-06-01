#!/bin/bash
img=pyftpdlib-docker
docker build -t $img . && \
docker run -it --rm -p 21:21 -p 30000-30009:30000-30009 -v file-servers:/ftp/file-servers $img
