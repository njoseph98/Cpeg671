mov eax, 11 ;sys_execve
call file:
.string "/bin/sh"
file:
pop ebx
xor ecx, ecx
xor edx, edx
int 0x80
