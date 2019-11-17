import threading as td
class print_in_order_reverse :
	'''def __init__(self,n):
		self.n=n
	'''	
	def order(self,n):
		print("InOrder.:",end=" ")
		i=1
		while(i<=n):
			print(i,end=" ")
			i+=1
		print("")
	
	def reverse(self,n):
		print("Reverse.:",end=" ")
		i=n
		while(i>0):
			print(i,end=" ")
			i-=1
		print("")
		
		
def main():
	n=int(input("Give no.:"))
	Obj1=print_in_order_reverse()
	t1=td.Thread(target=Obj1.order,args=(n,))
	t2=td.Thread(target=Obj1.reverse,args=(n,))
	t1.start()
	t1.join()
	t2.start()
	t2.join()
	
	

if __name__=="__main__":
	main()