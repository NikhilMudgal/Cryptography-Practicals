a=int(input())
b=int(input())
r1,r2=a,b
while r2!=0:
	c=r1%r2
	r1=r2
	r2=c
print("Gcd of "+ str(a)+" and "+str(b)+" is "+str(r1))
