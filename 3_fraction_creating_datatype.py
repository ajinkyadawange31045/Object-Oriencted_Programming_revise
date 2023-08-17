class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d
    def __str__(self) :
        return f"{self.num}/{self.den}"
    def __add__(self,other):
        #pehla object self ko milega and other will be with other, both have their own numerator and denominator
    #fraction addition is simple
        temp_num = self.num*other.den + other.num*self.den
        temp_den = self.den*other.den
        return f"{temp_num}/{temp_den}"


a = Fraction(4,5)
print(type(a))
print(a) #how it looks we need to show in class.
# we will use magic methods
# __str__


b = Fraction(1,2)
print(b)

# to add the objects a and b, we use the __add__ (magic methods)
print(a+b)

# for a-b
# we will use __sub__
print(a-b)

# same logic for multiplication, 
# numerator will be mulitplied with one other. and 
# magic method is __mul__


# __truediv__   
# for denomicator

