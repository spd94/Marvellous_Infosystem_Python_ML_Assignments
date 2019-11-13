def fact(n):
	c=1
	t=1
	while(c<=n):
		t=t*c
		c+=1
	print("Output : ",t)

print("Input :",end=" ")
x=int(input())
fact(x)