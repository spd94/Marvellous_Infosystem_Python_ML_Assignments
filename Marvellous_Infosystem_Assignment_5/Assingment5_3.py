
def accept_N(n):
	if(n>0):
		print(n,end=" ")
		accept_N(n-1)
	

if __name__ == "__main__": 
	print("Input :",end=" ")
	x=int(input())
	print("Output:",end=" ")
	accept_N(x)