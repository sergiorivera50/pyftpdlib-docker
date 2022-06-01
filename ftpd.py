import argparse
from server import serve

def main() -> None:
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
    '--user', default='root',
    help="Username for FTP access"
  )
  parser.add_argument(
    '--password', default='root',
    help="Password for the FTP user"
  )
  parser.add_argument('--host', default='0.0.0.0')
  parser.add_argument('--port', type=int, default=21)
  parser.add_argument(
    '--passive', default='30000-30009',
    help="Range of passive ports"
  )
  parser.add_argument(
    '--anon', action='store_true',
    help="Allows anonymous access"
  )
  args = parser.parse_args()
  serve(**vars(args))

if __name__ == '__main__':
  main()
