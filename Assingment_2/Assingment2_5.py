import math as m
def Chk_prime(n):
	c=0
	for i in range(2,int(m.sqrt(n))):
		if(n%i==0):c=1
	if(c==1):print("Output : It is not Prime Number")
	else:print("Output : It is Prime Number")
	
print("Input :",end=" ")
x=int(input())
Chk_prime(x)