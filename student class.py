class student:
    def __init__(self,name, roll,m1,m2,m3):
        self.name=name
        self.roll=roll
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def read(self):
        self.name=input("enter your name")
        self.roll=input("enter your roll no")
        self.m1=int(input("enter the marks of sub1"))
        self.m2=int(input("enter the marks of sub2"))
        self.m3=int(input("enter the marks of sub3"))
    def total(self):
        tot=self.m1+self.m2+self.m3
        print(tot)
    def display(self):
        print(f"student name: {self.name}")
        print(f"roll no: {self.roll}")
        print(f"sub1 marks: {self.m1}")
        print(f"sub2 marks: {self.m2}")
        print(f"sub3 marks: {self.m3}")
s1 = student("ash",68,90,92,93)
s1.read()
s1.display()
s1.total()

