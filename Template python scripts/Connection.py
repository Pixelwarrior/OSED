import socket
import logging
from datetime import datetime
import sys

# Global variables
dt = datetime.now()
logging.basicConfig(format='%(message)s', level=logging.DEBUG)



class Connection:
    def __init__(self, ip, port, buffer):
        self.ip = ip
        self.port = port
        self.buffer = buffer
    def sendBuffer(self):
        try:
            print("[+] Attempting to send buffer... ")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            print("[+] Connected to: {self.ip}")
            if len(self.buffer) > 0:
                for i in self.buffer:
                    print("[DEBUG] ", str(i))
                    s.send(i)
            else:
                print("[-] Buffer contained no information.")
                sys.exit()
            s.close()
            print("Buffer sent successfully")
        except socket.error as e:
            logging.info(str(dt) + " - Error: ", str(e))


