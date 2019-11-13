sum=0
c=0
def accept_N(n):
	global sum,c
	if(n>0):
		x=int(n%10)
		sum+=x
		accept_N(int(n/10))
	return sum
	

if __name__ == "__main__": 
	print("Input :",end=" ")
	x=accept_N(int(input()))
	print("Output:",x,end=" ")
	