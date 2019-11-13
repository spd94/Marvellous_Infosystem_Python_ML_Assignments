def accept_N_min(n):
	ls=list()
	i=0
	print("Input Elements :",end=" ")
	while(i<n):
			ls.append(int(input()))
			i+=1
	i=0
	sum=ls[0]
	while(i<n):
		if(sum>ls[i]):sum=ls[i]
		i+=1
	return(sum)



if __name__ == "__main__": 
	print("Input : Number of Elements :",end=" ")
	x=accept_N_min(int(input()))
	print("Output :",x,end=" ")