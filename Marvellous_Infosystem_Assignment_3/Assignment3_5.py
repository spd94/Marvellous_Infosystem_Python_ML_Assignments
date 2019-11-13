import MarvellousNum as mn

def ListPrime(n):
	ls=list()
	ps=list()
	i=0
	print("Input Elements :",end=" ")
	while(i<n):
			ls.append(int(input()))
			i+=1
	for i in range(0,len(ls)): 
		if(mn.ChkPrime(ls[i])):ps.append(ls[i])
	i=0
	sum=0
	
	while(i<len(ps)):
		sum+=ps[i]
		i+=1
	return(sum,ps)
	
	
if __name__ == "__main__": 
	print("Input : Number of Elements :",end=" ")
	x,ps=ListPrime(int(input()))
	i=0
	print("Output : ",x,end=" ")
	print("(",end="")
	while(i<len(ps)):
		print(ps[i],end="")
		if(i!=len(ps)-1):print(" + ",end="")
		i+=1
	print(")",end="")