def accept_N(n):
	ls=list()
	i=0
	sum=0
	print("Input Elements :",end=" ")
	while(i<n):
			ls.append(int(input()))
			i+=1
	i=0
	while(i<n):
		sum+=ls[i]
		i+=1
	return(sum)



if __name__ == "__main__": 
	print("Input : Number of Elements :",end=" ")
	x=accept_N(int(input()))
	print("Output :",x,end=" ")