import os

def mkdir(dir) -> None:
  if not os.path.isdir(dir):
    os.mkdir(dir)
