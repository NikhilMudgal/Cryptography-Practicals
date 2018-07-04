a=int(input())
b=int(input())
s1=1
s2=0
t1=0
t2=1

r1,r2=a,b
while r2!=0:
	q=int(r1/r2)
	c=r1%r2
	r1=r2
	r2=c
	s=s1-q*s2
	s1=s2
	s2=s
	t=t1-q*t2
	t1=t2
	t2=t
print("Gcd of "+ str(a)+" and "+str(b)+" is "+str(r1))
print("S= "+str(s1))
print("T= "+str(t1))
print(s1*a+t1*b)
