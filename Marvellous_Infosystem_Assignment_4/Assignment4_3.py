from functools import reduce
def accept_N_elem(n):
	ls=list()
	i=0
	sum=0
	print("Input Elements :",end=" ")
	while(i<n):
			ls.append(int(input()))
			i+=1
	fl=list(filter(lambda x:(70<=x<=90),ls))
	print("List after filter :",end=" ")
	print(fl)
	ml=list(map(lambda x:x+10,fl))
	print("List after map :",end=" ")
	print(ml)
	prd=reduce(lambda x,y: x*y,ml)
	return prd

if __name__ == "__main__": 
	print("Input : Number of Elements :",end=" ")
	x=accept_N_elem(int(input()))
	print("Output of reduce :",x,end=" ")