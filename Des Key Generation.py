def parity_drop(s):
        operate=[]
        p_drop_table=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
        for i in range(56):
                operate.append(0)
        for i in range(56):
                operate[i]=s[p_drop_table[i]-1]
        return operate
def compression(s):
        operate=[]
        compression_table=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
        for i in range(48):
                operate.append(0)
        for i in range(48):
                operate[i]=s[compression_table[i]-1]
        return operate
key=input("Input key to convert hexadecimal to binary ")
a=bin(int(key,16))
op=parity_drop(a[::-1])
right=int(''.join(op[:28]),2 )
left=int(''.join(op[28:]),2 )
for i in range(1,17):
	if( i in [1,2,9,16] ):
		left= (left<<1) | (left>>27)	
		right= (right<<1) | (right>>27) 
	else:
		left= (left<<2) | (left>>26)  
		right= (right<<2) | (right>>26) 
	l=bin(left)
	r=bin(right)
	ls=str(l[2:])
	rs=str(r[2:])
	op=''.join( compression(ls+rs))  
	print('round'+str(i)+' key= '+ hex(int(op,2)) )
