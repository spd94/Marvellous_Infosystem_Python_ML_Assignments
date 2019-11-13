import Arithmetic as ar
c=1
print("Enter 2 no.")
a=int(input())
b=int(input())
while(c):
	print("----Press---- \n1.Add()\n2.Sub()\n3.Mult()\n4.Div()\n5.Give no.\n0 for exit")
	c=int(input())
	if(c==1):print("Add.:",ar.Add(a,b))
	elif(c==2):print("Sub.:",ar.Sub(a,b))
	elif(c==3):
			if(b!=0):print("Mult.:",ar.Mult(a,b))
			else:print("Denominator must > 0")
	elif(c==4):print("Div.:",ar.Div(a,b))
	elif(c==5):
			print("Enter 2 no.")
			a=int(input())
			b=int(input())
	elif(c==0): break
	else:print("Invalid option")
	
	

	