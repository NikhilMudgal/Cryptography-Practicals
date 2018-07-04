k=int(input("Enter the key value"))
d=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d1={}
d2={}
D=[]
for i in range(0,len(d)):
    d1[d[i]]=i

for i in d:
    a=i.upper()
    D.append(a)
for i in range(0,len(D)):
    d2[D[i]]=i

eD=[]
d3=[]

text=input("Enter the text to be encrypted ")
for i in text:
    if(i==" "):
        eD.append(26)
    else:
        a=d1[i]+k
        a=a%26
        eD.append(a)
for i in range(len(eD)):
    
    if(eD[i]==26):
        d3.insert(i," ")
    else:
        y=eD[i]
        s=[ x for x in d2.keys() if d2[x] ==y  ]
        t=''.join(s)
        d3.append(t)
t=''.join(d3)
print(t)        

#Decryption
ed=[]
def Decrypt():
    d=""
    for i in t:
        if i==" ":
            d+=i
        else:
            i=ord(i)-65-k
            character=chr((i%26)+97)
            d+=character
    print(d)
Decrypt()
