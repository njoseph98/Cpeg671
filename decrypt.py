def decrypt(arg_0):
    #getting values from hex to dec
    a =int ("AAAA", 16) 
    b=int("7B", 16)
    #reversing encrypt function
    x=arg_0 ^ a
    x=x/21
    return x-b

a=int("A000",16)
print(decrypt(a))

b=int("A17A", 16)
print(decrypt(b))

c=int("A608", 16)
print(decrypt(c))

d=int("A42F", 16)
print(decrypt(d))

e=int("A150",16)
print(decrypt(e))