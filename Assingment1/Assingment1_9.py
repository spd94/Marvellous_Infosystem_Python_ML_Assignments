def First_n_even(n):
	print("Output :",end=" ")
	c=0
	i=2
	while(c<n):
		if(i%2==0): 
			print(i,end=" ")
			c+=1
		i+=1
First_n_even(10)