class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the ATM Machine")

	def deposit(self):
		amount=float(input("Enter Amount to be Deposited: "))
		self.balance += amount
		print("Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter Amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("You Withdrew:", amount)
		else:
			print("Insufficient balance ")

	def display(self):
		print("Available Balance is",self.balance)


s = Bank_Account()
s.deposit()
s.withdraw()
s.display()

