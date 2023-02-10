import socket
from datetime import datetime
import os

class Buffer:


    def __init__(self, ip, port, buffer, cn):
        self.ip = ip
        self.port = port
        self.buffer = buffer
        self.cn = cn
    def getIP(self):
        return self.ip
    def getPort(self):
        return self.port
    def connect(self):
        dt = datetime.now()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
             s.connect((self.ip, self.port))
             if self.cn > 0:
                    for i in self.buffer:
                        print(i)
                        s.send(i)
                        print(s.recv(1024))
             else:
                    print("Please provide a value for the send count. ")
                    os.close()
             print(str(dt) + " - Buffer sent " + self.ip)
        except socket.error as e:
            print(str(dt) + " - Failed to send buffer to " + self.ip)
        except Exception as e:
            print(str(dt) + " - Error: ", str(e))
