'''data -> balence lagega, 
        atm pin is also required

functions (methods) -> withdraw, check balance, withdraw, create bill'''

class Atm:
        #this is constructor
        def __init__(self):
                print('inside constructor')
                self.pin = ""
                self.balance = 0



        def menu(self):
                user_input = input("""
hello, how woud you like to preceed?
1. Enter 1 to create pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. enter 4 to check balance
5. enter 5 to exit 
: -> """)
                if user_input == '1':
                        # print('create print')
                        self.create_pin()
                elif user_input == '3':
                        self.withdraw()
                elif user_input == '2':
                        self.deposit()
                elif user_input == '4':
                        self.check_balance()
                else:
                        print('exit')

        def create_pin(self):
                self.pin = input('enter your pin : ')
                print('pin set successfully')
            
        def deposit(self):
                temp = input('Enter your pin:')
                if temp == self.pin:
                        amount = int(input('Enter the amount: '))
                        self.balance = self.balance + amount
                else:
                        print('invalid pin')

        def withdraw(self):
                temp = input('Enter your pin:')
                if temp == self.pin:
                        amount = int(input('Enter the amount: '))
                        if amount<self.balance:
                                self.balance = self.balance - amount
                        else:
                                print('Insfficient funds')
                else:
                        print('invalid print')
        
        def check_balance(self):
                temp = input('Enter your pin:')
                if temp == self.pin:
                        print(self.balance)
                else:
                        print('invalid pin')
    
a = Atm()
a.menu()
