# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter. 
import math
class Circle:
    rad = int(input('Enter the radius of the circle: '))
    def area_of_circle(self):
        area = math.pi*(self.rad)*(self.rad)
        print(area)
    
    def perimeter_of_circle(self):
        peri = 2*math.pi*(self.rad)
        print(peri)

obj = Circle()
obj.area_of_circle()
obj.perimeter_of_circle()