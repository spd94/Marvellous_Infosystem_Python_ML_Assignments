class Demo:
	Value=1
	def __init__(self,x,y):
		self.no1=x
		self.no2=y
	def Fun(self):
		print("no1 :",self.no1)
	def Gun(self):
		print("no2 :",self.no2)

def main():
		Obj1 = Demo(11,21)
		Obj2 = Demo(51,101) 
		Obj1.Fun()
		Obj2.Fun()
		Obj1.Gun()
		Obj2.Gun() 


if __name__ == "__main__": 
	main()