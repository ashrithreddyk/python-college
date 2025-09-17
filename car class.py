class car:
    def __init__(self,name="", modelno="",year=0,price=0,fe=0):
        self.name=name
        self.modelno=modelno
        self.year=year
        self.price=price
        self.fe=fe
    def read(self):
        self.name=input("enter your name")
        self.modelno=input("enter your modelno")
        self.year=int(input("enter year"))
        self.price=int(input("enter the price"))
        self.fe=int(input("enter the fuel effeciency"))
    def display(self):
        print(f"student name: {self.name}")
        print(f"modelno: {self.modelno}")
        print(f"year: {self.year}")
        print(f"price: {self.price}")
        print(f"fe: {self.fe}")
s1 = car()
s1.read()
s1.display()
