n=int(input())
count=0

for i in range(2,n):
	if(n%i)==0:
		count=count+1

if count==0:	
	print("Number "+str(n)+" is prime")
	b=int(input("Enter the number whose multiplicative inverse is to be calculated "))
	t1,t2=0,1
	r1,r2=n,b
	while r2>0:
		q=int(r1/r2)
		r=r1-q*r2
		r1,r2=r2,r
		t=t1-q*t2
		t1,t2=t2,t
	if(r1==1):
		if(t1<0):
			t1=t1+n
			print(t1)
		else:
			print(t1)
	else:
		print("multiplicative inverse doesnot exist")

else:
	print("Number "+str(n)+ " is not prime")
