class Calculator:
    num=100
    num1=200
    num2=300

    #default constructor
    def __init__(self,a,b):
        self.firstnumber=a
        self.secondnumber=b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing a method in a class")

    def Summation(self):
        return self.firstnumber + self.secondnumber

    def getName(self):
        print("My name is Pradip")

    def getAge(self):
        print("I am 27 years old")

obj = Calculator(2,3)

obj.getData()
obj.getName()
obj.getAge()
print(obj.num)
print(obj.num1)
print(obj.num2)
print(obj.Summation())

obj1=Calculator(4,5)
obj1.getData()
print(obj1.num)
print(obj1.Summation())