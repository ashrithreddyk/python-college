class bank_account():
    def __init__(self,name="",balance=0,choice1="",choice2="",amt2d=0,amt2w=0):
        self.name=name
        self.balance=balance
        self.choice1=choice1
        self.choice2=choice2
        self.amt2d=amt2d
        self.amt2w=amt2w
    def read(self):
        self.name=input("enter the name")
        self.balance=int(input("enter the balance"))
    def deposit(self):
        self.choice1=input("would you like to deposit")
        if self.choice1=="yes":
            self.amt2d=int(input("enter the amount to be deposited"))
            self.balance+=self.amt2d
    def withdraw(self):
        self.choice2=input(("Would you like to withdraw"))
        if self.choice2=="yes":
            self.amt2w=int(input("enter the amount to be withdrawn"))
            self.balance-=self.amt2w
    def display(self):
        print(f"name: {self.name}")
        print(f"balance: {self.balance}")
b1=bank_account()
b1.read()
b1.deposit()
b1.withdraw()
b1.display()