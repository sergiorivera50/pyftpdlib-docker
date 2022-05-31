from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def serve():
  authorizer = DummyAuthorizer()

  authorizer.add_user('root', 'root', './file-servers/auth-fs/', perm='elradfmwMT')
  authorizer.add_anonymous('./file-servers/anon-fs/')

  handler = FTPHandler
  handler.authorizer = authorizer
  handler.permit_foreign_addresses = True
  handler.banner = "pyftpdlib FTP Server"
  handler.passive_ports = range(3000, 3010)

  address = ("", 21)
  server = FTPServer(address, handler)

  server.max_cons = 256
  server.max_cons_per_ip = 5

  server.serve_forever()

if __name__ == '__main__':
  serve()
