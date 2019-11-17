import threading as td
class odd_even_thread:
	'''def __init__(self,n):
		self.n=n
	'''	
	def even(self,n):
		print("Even factor sum.:",end=" ")
		sum=0
		for i in n:
			if(i%2==0):
				sum+=i
				#print(i,end=" ")
		print("",sum)
		
	def odd(self,n):
		print("Odd Factor Sum.:",end=" ")
		sum=0
		for i in n:
			if(i%2!=0):
				sum+=i
				#print(i,end=" ")
		print("",sum)
		
def main():
	n=[10,22,12,12,1,5,15,81,418,13,5,71,45,4,21]
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