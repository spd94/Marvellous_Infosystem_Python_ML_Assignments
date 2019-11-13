from functools import reduce
import math 
def ChkPrime(n):
	c=0
	for i in range(2,int(math.sqrt(n))+1):
		if(n%i==0):c=1
	if(c==0):return(n)

def max_list(n,y):
	if(n>y):return(n)
	else: return(y)

def accept_N_elem(n):
	ls=list()
	i=0
	sum=0
	print("Input Elements :",end=" ")
	while(i<n):
			ls.append(int(input()))
			i+=1
	fl=list(filter(ChkPrime,ls))
	print("List after filter :",end=" ")
	print(fl)
	ml=list(map(lambda x:x*2,fl))
	print("List after map :",end=" ")
	print(ml)
	prd=reduce(max_list,ml)
	return prd

if __name__ == "__main__": 
	print("Input : Number of Elements :",end=" ")
	x=accept_N_elem(int(input()))
	print("Output of reduce :",x,end=" ")