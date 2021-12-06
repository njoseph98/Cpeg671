from pwn import *

#from last
vals=[0x23232323, 0x54545454, 0x11111111, 0x43434343, 0x11111111, 0x57575757, 0x32323232, 0xdfdfdfdf]
order=[2,5,3,0,7,1,4,6]
output=b''
#little indian, reverse vals
vals.reverse()
reversedVals=vals
for num in range(len(reversedVals)):
    #xor
    reversedVals[num]=reversedVals[num] ^ (num*0xaaaa)
val=0

#swapping
while(val<len(reversedVals)):
    tmp=reversedVals[order[val+1]]
    reversedVals[order[val+1]]=reversedVals[order[val]]
    reversedVals[order[val]]=tmp
    val+=2

for finalNum in range(len(reversedVals)):
    output+=p32(reversedVals[finalNum])
print(output)