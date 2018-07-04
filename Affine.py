km=int(input("Enter the key for multiplication and division "))
ka=int(input("Enter the key for addition and subtraction "))
text=input("Enter the text to be encrypted ")
encr=""
for i in text:
    if i==" ":
        encr+=i
    else:
        c=(ord(i)-97)*km
        c+=ka
        c=c%26
        c=chr(c+65)
        encr+=c
print(encr)
