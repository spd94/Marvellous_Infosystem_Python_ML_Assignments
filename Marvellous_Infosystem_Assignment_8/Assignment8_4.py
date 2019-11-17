import threading as td
class count_CSD:
	'''def __init__(self,n):
		self.n=n
	'''	
	def Chk_CSD(self,x,m):
		if(m=="C"):
			c=0
			for i in x:
				if(i.isupper()):
					c+=1
			print("Capital character count.: ",c)
			
		elif(m=="S"):
			c=0
			for i in x:
				if(i.islower()):
					c+=1
			print("Small character count.: ",c)
			
		elif(m=="D"):
			c=0
			for i in x:
				if(i.isdigit()):
					c+=1
			print("Digit count.: ",c)
			
		else:
			print("Give mode to check on string,C:Capital	S:Small		D:Digit")
		
		
		
def main():
	n=input("Give string.:")
	Obj1=count_CSD()
	t1=td.Thread(target=Obj1.Chk_CSD,args=(n,"C",))
	t2=td.Thread(target=Obj1.Chk_CSD,args=(n,"S",))
	t3=td.Thread(target=Obj1.Chk_CSD,args=(n,"D",))
	t1.start()
	#t1.join()
	t2.start()
	#t2.join()
	t3.start()
	#t3.join()
	print("Exit from main")
	

if __name__=="__main__":
	main()