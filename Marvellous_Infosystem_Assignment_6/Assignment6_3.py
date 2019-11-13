class Arithmetic:
	def __init__(self):
		self.Value1=0
		self.Value2=0
	def Accept(self):
		self.Value1=int(input("Give 2 nos."))
		self.Value2=int(input())
	def Addition(self):
		#print("Addition=",self.Value1+self.Value2)
		return self.Value1+self.Value2
	def Substraction(self):
		#print("Substraction=",self.Value1-self.Value2)
		return self.Value1-self.Value2
	def Multiplication(self):
		#print("Multiplication=",self.Value1*self.Value2)
		return self.Value1*self.Value2
	def Division(self):
		#print("Division=",self.Value1/self.Value2)
		return self.Value1/self.Value2

def main():
		Obj1=Arithmetic()
		Obj1.Accept()
		result=Obj1.Addition()
		print("Addition result=",result)
		result=Obj1.Substraction()
		print("Substraction result=",result)
		result=Obj1.Multiplication()
		print("Multiplication result=",result)
		result=Obj1.Division()
		print("Division result=",result)

if __name__ == "__main__": 
	main()