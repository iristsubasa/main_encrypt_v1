import base64
import getpass
# enctry 
def enctry(s):
    k = 'abcdefg1234567890454342456245245324545'
    encry_str = ""
    for i,j in zip(s,k): 
        temp = str(ord(i)+ord(j))+'_' 
        encry_str = encry_str + temp
    s1 = base64.b64encode(encry_str.encode("utf-8"))
    return s1

# dectry
def dectry(s2):
    p = base64.b64decode(s2).decode("utf-8")
    k = 'abcdefg1234567890454342456245245324545'
    dec_str = ""
    for i,j in zip(p.split("_")[:-1],k):  
        temp = chr(int(i) - ord(j)) 
        dec_str = dec_str+temp
    return dec_str

# a1 = enctry()
a2 = dectry('MTk1XzE0OF8yMzNfMjA0XzE2OV8yMjZfMjI2XzE1Nl8xNzVfMTcxXw==')
print(a2)