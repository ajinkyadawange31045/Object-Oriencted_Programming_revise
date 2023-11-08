# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. 

import datetime
class Person:
    name = input('Enter the name of the person: ')
    country = input('Enter your country: ')
    date_of_birth = input('Enter date of birth (dd/mm/yyyy): ')

    def age(self):
        birth_year = int(self.date_of_birth[-4:])
        age = 2023 - birth_year
        print(age)

obj = Person()
obj.age()