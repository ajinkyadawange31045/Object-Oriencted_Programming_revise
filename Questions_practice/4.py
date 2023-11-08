# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square. 

class Shape:
    def __init__(Self):
        print("Area of the shape are as follows, please enter accordingly ")
    def details(self):
        pass

class Triangle(Shape):
    def details(self):
        base = int(input('enter base: '))
        h = int(input('enter height of the triangle: '))
        area = 0.5*base*h
        print('area of traingle: ' ,area)

class Square(Shape):
    def details(self):
        side = int(input('enter side of the square: '))
        area = side*side
        print('area of Square: ' ,area)

class Circle(Shape):
    def details(self):
        r = int(input('Enter the radius of the circle: '))
        area = 3.14*r*r
        print('area of Circle: ' ,area)

obj = Square()
obj.details()
obj = Triangle()
obj.details()
obj = Circle()
obj.details()