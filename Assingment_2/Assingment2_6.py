def print_pattern_desc(n):	
	i=n
	print("Output :")
	while(i>0):
		j=i
		while(j>0):
			print("*",end=" ")
			j-=1
		print("")
		i-=1
print("Input :",end=" ")
x=int(input())
print_pattern_desc(x)