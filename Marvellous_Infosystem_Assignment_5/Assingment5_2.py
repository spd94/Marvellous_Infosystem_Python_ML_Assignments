c=0
i=1
def accept_N(n):
	global i,c
	if(i==1):c=n
	if(c>=i):
		print(i,end=" ")
		i+=1
		accept_N(i)
	

if __name__ == "__main__": 
	print("Input :",end=" ")
	x=int(input())
	print("Output:",end=" ")
	accept_N(x)