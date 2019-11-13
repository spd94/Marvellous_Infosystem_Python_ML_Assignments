sum=1

def accept_N(n):
	global sum
	if(n>0):
		sum*=n
		accept_N(n-1)
	return sum
	

if __name__ == "__main__": 
	print("Input :",end=" ")
	x=accept_N(int(input()))
	print("Output:",x,end=" ")
	