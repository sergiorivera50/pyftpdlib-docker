import os.path
from helper import mkdir

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

FTP_ROOT = '/ftp/file-servers'

def serve(user: str, password: str, host: str, port: int, passive: str, anon: bool) -> None:
  authorizer = DummyAuthorizer()

  # Create authorized users

  user_dir = os.path.join(FTP_ROOT, user)
  mkdir(user_dir)
  authorizer.add_user(user, password, user_dir, perm='elradfmwMT')

  if anon:
    anon_dir = os.path.join(FTP_ROOT, 'anon')
    mkdir(anon_dir)
    authorizer.add_anonymous(anon_dir)

  # Setup FTP handler

  handler = FTPHandler
  handler.authorizer = authorizer
  handler.permit_foreign_addresses = True

  passive_ports = [int(port) for port in passive.split('-')]
  assert len(passive_ports) == 2
  handler.passive_ports = range(passive_ports[0], passive_ports[1])

  server = FTPServer((host, port), handler)
  server.max_cons = 256
  server.max_cons_per_ip = 5
  server.serve_forever()
