class Circle:
	PI=3.14
	def __init__(self):
		self.Radius=0
		self.Area=0
		self.Circumference=0
	def Accept(self):
		#self.Radius,self.Area,self.Circumference=int(input("Enter Radius,Area,Circumference"),input(),input())
		self.Radius=int(input("Enter Radius :"))
		
	def CalculateArea(self):
		self.Area=Circle.PI*(self.Radius**2)
	def CalculateCircumference(self):
		self.Circumference=Circle.PI*(self.Radius*2)
	def Display(self):
		print("Radius={} Area={} Circumference={}".format(self.Radius,self.Area,self.Circumference))

def main():
		Obj1=Circle()
		Obj1.Accept()
		Obj1.CalculateArea()
		Obj1.CalculateCircumference()
		Obj1.Display()


if __name__ == "__main__": 
	main()