class BankAccount:
    def __init__(self, bal, name):
        self.balance = bal
        self.name = name

    def greet_balance(self):
        print('Hello {}, your balance is ${}.'.format(self.name, self.balance))

    def withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('You have withdrawn ${}, your balance is now ${}.'.format(amount, self.balance))
        else:
            print('You don\'t have enought money dude.')

    def deposit(self, amount):
        self.balance += amount
        print('You deposit ${}'.format(amount))


class BankAccountRestricted(BankAccount):
    def __init__(self, bal, name, padding):
        BankAccount.__init__(self, bal, name)
        self.padding = padding

    def withdrawal(self, amount):
        if self.balance - amount - self.padding >= 0:
            self.balance -= amount
            print('You have withdrawn ${}, your balance is now ${}.'.format(amount, self.balance))
        else:
            print('You don\'t have enought money dude.')

chris = BankAccountRestricted(150, 'Chris', 20)
katie = BankAccount(2000, 'Katie')


chris.greet_balance()
# katie.greet_balance()

# chris.withdrawal(101)
# chris.withdrawal(30)
