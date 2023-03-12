import socket
import logging
import sys
from time import sleep

logging.basicConfig(level=logging.INFO)

class Connection:
    def __init__(self, ip: str, port: int, buffer_data: bytes):
        self.ip = ip
        self.port = port
        self.buffer_data = buffer_data
    def sendBuffer(self):
        print(f"[+] Buffer: ", str(self.buffer_data))
        try:
            with socket.create_connection((self.ip, self.port), timeout=10) as sock:
                logging.info(f"[+] Attempting to send buffer")
                sock.send(self.buffer_data)
                recv = sock.recv(1024)
                print(recv)
                sleep(1)
                logging.info(f"[+] Buffer sent!")
        except TimeoutError:
            logging.info(f"Connection to {self.ip} timed out")
        except ConnectionRefusedError:
            logging.info(f"Connection to {self.ip} refused")
        except Exception as e:
            logging.info(f"Error: ", str(e))


            
