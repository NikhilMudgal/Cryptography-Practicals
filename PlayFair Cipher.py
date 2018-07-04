from random import randint
b=0
k=input("Enter the key ")
l=input("Enter the text to be encrypted ")
l1=[]
for x in k.upper():
	if x not in l1:
		l1.append(x)

ch="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in ch.upper():
	if x not in l1:
		l1.append(x)

c=l1.index('I')
d=l1.index('J')

l1.remove('I')
l1.remove('J')
if c<d:
	l1.insert(c,'I/J')
else:
	l1.insert(d,'I/J')

matrix=[]

for x in range(0,5):
	temp=[]
	for y in range(5):
		temp.append(l1[0])
		del l1[0]	
	matrix.append(temp)

print(matrix)

while b!=1:
	a=randint(65,91)
	a=chr(a)
	if a not in l.upper():
		b=1

l3=list(l.upper()) 

enc=""
temp=[]
for x in range(0,len(l3)):
	if l3[x]==l3[x+1]:
		l3.insert(x+1,a)
if len(l3)%2!=0:
	l3.append(a)

l2=[] #for pairing
for x in range(0,len(l3),2):
	temp=[]
	temp.extend((l3[x],l3[x+1]))
	l2.append(temp)
p=q=r=s=-1
temp=[]
for i in range(len(l2)):
	w,z=l2[i][0],l2[i][1]
	for x in range(0,5):
		for y in range(0,5):
			if matrix[x][y]==w:
				p,q=x,y
			if matrix[x][y]==z:
				r,s=x,y
	if p==r:
		temp.append(matrix[p][(q+1)%5])
		temp.append(matrix[r][(s+1)%5])
	elif q==s:
		temp.append(matrix[(p+1)%5][q])
		temp.append(matrix[(r+1)%5][s])
	else:
		temp.append(matrix[p][s])
		temp.append(matrix[r][q])
result=[]
result=['I' if x=='I/J' else x for x in temp]
enc=''.join(result)
print(enc)
