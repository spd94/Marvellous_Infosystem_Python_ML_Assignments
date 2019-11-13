def accept_N_freq(n):
	ls=list()
	i=0
	print("Input Elements :",end=" ")
	while(i<n):
			ls.append(int(input()))
			i+=1
	i=0
	print("Elements to search :",end=" ")
	x=int(input())
	sum=0
	while(i<n):
		if(x==ls[i]):sum+=1
		i+=1
	return(sum)



if __name__ == "__main__": 
	print("Input : Number of Elements :",end=" ")
	x=accept_N_freq(int(input()))
	print("Output :",x,end=" ")