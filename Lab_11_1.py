from pwn import p32

"""
23
23
23
23
54
54
54
54
11(4)
43(4)
11(4)
57(4)
32(4)
34(4)
"""
#in order
first=p32(0x23232323)
second=p32(0x54545454)
third=p32(0x11111111)
four=p32(0x43434343)
five=third
six=p32(0x57575757)
seven=p32(0x32323232)
eight=p32(0x34343434)

#reverse
test=eight+seven+six+five+four+third+second+first
print(test)