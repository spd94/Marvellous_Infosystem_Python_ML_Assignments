import threading as td
class odd_even_thread:
	def __init__(self,n):
		self.n=n
		
	def even(self):
		print("Even.:",end=" ")
		for i in range(2,self.n+1):
			if(i%2==0):print(i,end=" ")
		print("")
		
	def odd(self):
		print("Odd.:",end=" ")
		for i in range(2,self.n+1):
			if(i%2!=0):print(i,end=" ")
		print("")
def main():
	n=int(input("Give n.:"))
	Obj1=odd_even_thread(n)
	t1=td.Thread(target=Obj1.even,args="")
	t2=td.Thread(target=Obj1.odd,args="")
	t1.start()
	t1.join()
	t2.start()
	t2.join()
	print("Exit from main")
	

if __name__=="__main__":
	main()