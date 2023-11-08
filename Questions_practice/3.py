# 3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations. 

class Calculator:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    def add(self):
        operation = self.a+self.b
        print(operation)

    def sub(self):
        operation = self.a-self.b
        print(operation)

    def mul(self):
        operation = self.a*self.b
        print(operation)

    def div(self):
        operation = self.a/self.b
        print(operation)

    def reminder(self):
        operation = self.a%self.b
        print(operation)

obj = Calculator()
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.reminder()
