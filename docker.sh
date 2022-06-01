#!/bin/bash

while true; do
  read -s -p "Password for root FTP user: " ROOT_PASS_INPUT
  echo
  read -s -p "Confirm password: " ROOT_PASS_CONFIRM
  echo
  [ "$ROOT_PASS_INPUT" = "$ROOT_PASS_CONFIRM" ] && break
  echo "Passwords don't match. Please try again..."
done

echo "Building Docker image..."
img=pyftpdlib-docker
docker build -t $img . \
&& docker run -it --rm -p 21:21 -p 30000-30009:30000-30009 -e ROOT_PASS=$ROOT_PASS_CONFIRM -v file-servers:/ftp/file-servers $img
