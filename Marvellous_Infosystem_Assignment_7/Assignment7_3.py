import math as m
class Numbers:
	def __init__(self,no):
		self.Value=no
	def ChkPrime(self):
		c=0
		for i in range(2,int(m.sqrt(self.Value))):
			if(self.Value%i==0):c=1
		if(c==1):
			return False
		else:
			return True
	
	def SumFactors(self):
			c=0
			for i in range(1,self.Value):
				if(self.Value%i==0):c+=i
			return(c)
			
	def ChkPerfect(self):
		if(self.Value==self.SumFactors()): return True
		else:return False
	
	def Factors(self):
			c=0
			for i in range(1,self.Value):
				if(self.Value%i==0):print(i,end=" ")
			print("")
			
def main():
		Obj1=Numbers(int(input("Give Number.:")))
		if(Obj1.ChkPrime()):print("It's Prime no")
		else:print("It's not Prime no")
		if(Obj1.ChkPerfect()):print("It's Perfect no ")
		else:print("It's not Perfect no")
		print("Sum of Factors=",Obj1.SumFactors())
		print("Factors=",end="")
		Obj1.Factors()
		
		Obj2=Numbers(int(input("Give Number.:")))
		if(Obj2.ChkPrime()):print("It's Prime no")
		else:print("It's not Prime")
		if(Obj2.ChkPerfect()):print("It's Perfect no ")
		else:print("It's not Perfect no")
		print("Sum of Factors=",Obj2.SumFactors())
		print("Factors=",end="")
		Obj2.Factors()
		
if __name__ == "__main__": 
	main()
	