def sum_digits(n):
	t=0
	while(n>0):
		t=t+n%10
		n=n//10
	print("Output : ",t)
print("Input :",end=" ")
x=int(input())
sum_digits(x)