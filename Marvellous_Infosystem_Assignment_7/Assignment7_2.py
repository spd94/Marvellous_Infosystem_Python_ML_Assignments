class BankAccount:
	ROI=10.5
	def __init__(self,name,amt):
		self.Name=name
		self.Amount=amt
	def Display(self):
		print("----------(Customer Info)----------")
		print("Name= {} Amount= {}".format(self.Name,self.Amount))
		print("-----------------------------------")
		
	def Deposit(self):
		self.Amount+=int(input("Enter Amount to Add/Deposit.:"))
		print("Updated Balance =",self.Amount)
	def Withdraw(self):
		wa=int(input("Give Amount to Withdraw.:"))
		if(wa<self.Amount):
			self.Amount-=wa
			print("Amount Withdrawn = {} Successful, Available Balance= {}".format(wa,self.Amount))
		else:
			print("Failed, Amount to be Withdrawn = {} exceeds Available Balance= {}".format(wa,self.Amount))
	def CalculateIntrest(self):
			t=int(input("Enter Time for claculating Interest .:"))
			print("Claculate Interest Amount = ",(self.Amount*BankAccount.ROI*t)/100)
						
def main():
		Obj1=BankAccount("Sam",2000)
		Obj1.Display()
		Obj1.Deposit()
		Obj1.CalculateIntrest()
		Obj1.Withdraw()
		Obj1.Display()
		
		Obj2=BankAccount("Ram",2000)
		Obj2.Display()
		Obj2.Deposit()
		Obj2.CalculateIntrest()
		Obj2.Withdraw()
		Obj2.Display()
		
if __name__ == "__main__": 
	main()
		