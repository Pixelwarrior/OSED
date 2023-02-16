import Connection
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--server", help="IP of the server")
    parser.add_argument("-p", "--port", help="Port of the server")
    args = parser.parse_args()
    
    
    fullBuffer = b"A" * 2000
    connectionSettings = [fullBuffer]
    buf = Connection.Connection(args.server, int(args.port), connectionSettings)
    buf.sendBuffer()
if __name__ == '__main__':
    main()
