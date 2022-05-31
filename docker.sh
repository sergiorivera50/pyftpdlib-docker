#!/bin/bash
img=pyftpdlib-docker
docker build -t $img .
docker run -it --rm -p 21:21 -v $(pwd)/file-servers:/ftp/file-servers $img
