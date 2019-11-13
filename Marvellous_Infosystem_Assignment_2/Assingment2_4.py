def fac_add(n):
	c=0
	for i in range(1,n):
		if(n%i==0):c+=i
	print("Output : ",c)
print("Input :",end=" ")
x=int(input())
fac_add(x)