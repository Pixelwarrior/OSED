import buffer_test
def main():

    
    
    fullBuffer = b"A" * 2000
    connectionSettings = [fullBuffer]
    buf = buffer_test.Buffer("127.0.0.1", 80, connectionSettings, len(connectionSettings))
    buf.connect()
if __name__ == '__main__':
    main()
