import threading as td
class odd_even_thread:
	'''def __init__(self,n):
		self.n=n
	'''	
	def even(self,n):
		print("Even factor sum.:",end=" ")
		sum=0
		for i in range(2,n):
			if(i%2==0 and n%i==0):
				sum+=i
				#print(i,end=" ")
		print("",sum)
		
	def odd(self,n):
		print("Odd Factor Sum.:",end=" ")
		sum=0
		for i in range(2,n):
			if(i%2!=0 and n%i==0):
				sum+=i
				#print(i,end=" ")
		print("",sum)
		
def main():
	n=int(input("Give n.:"))
	Obj1=odd_even_thread()
	t1=td.Thread(target=Obj1.even,args=(n,))
	t2=td.Thread(target=Obj1.odd,args=(n,))
	t1.start()
	t1.join()
	t2.start()
	t2.join()
	print("Exit from main")
	

if __name__=="__main__":
	main()