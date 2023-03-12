import connection

def constructBuffer(ip, port):
    inputBuffer = b""
    inputBuffer += b"A" * 4000
    con = connection.Connection(ip, port, inputBuffer)
    con.sendBuffer()
def main():
    connectionSettings = ['127.0.0.1', '80']

    constructBuffer(connectionSettings[0], int(connectionSettings[1]))


if __name__ == "__main__":
    main()
