;create file
mov eax, 8 ;;sys_create
call file:
.string "/tmp/syscall.txt"
file:
pop ebx
mov ecx, 0777 ; need for permissions
int 0x80
push eax

;write to file
mov ebx, eax
mov eax, 4 ;sys write
call write:
.string "System Calls are cool!"
write:
pop ecx
mov edx, 22
int 0x80

;close the filename
mov eax, 6 ;sys close
pop ebx
mov ecx, 0
mov edx, 0
int 0x80

; exit
mov eax, 1 ;sys exit
mov ebx, 0
mov ecx, 0
mov edx, 0
int 0x80