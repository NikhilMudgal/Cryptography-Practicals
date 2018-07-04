s_box=[[4,3,2,1],[7,5,6,8],[0,12,11,9],[15,13,14,10]]
input_num=input("Input a 4 bit binary string ")	
row_bit_1=input_num[0]
row_bit_2=input_num[-1]
column_bits=input_num[1:-1] 
r = int(row_bit_1 + row_bit_2,2)
c = int(column_bits,2)
n = s_box[r][c]
print(n)
output=bin(n)[2:]
print(output)
