class Customer:
    def __init__(self,name,gender) -> None:
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == 'Male':
        print('hello',customer.name,'sir')
    elif customer.gender == 'Female':
        print('hello',customer.name,'mam')
    else:
        print('hello',customer.name)

a = Customer('Ajinkya','Male')
print(a.name)
greet(a) #class ke object to ek function mai, diya, hai, so customer can also access that data.