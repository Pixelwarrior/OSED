import Connection
def main():

    
    
    fullBuffer = b"A" * 2000
    connectionSettings = [fullBuffer]
    buf = Connection.Connection("127.0.0.1", 80, connectionSettings, len(connectionSettings))
    buf.sendBuffer()
if __name__ == '__main__':
    main()
