def print_pattern(n):	
	i=1
	print("Output :")
	while(i<=n):
		j=1
		k=1
		while(j<=i):
			print(k,end=" ")
			k+=1
			j+=1
		print("")
		i+=1
print("Input :",end=" ")
x=int(input())
print_pattern(x)