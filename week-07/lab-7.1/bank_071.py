#!/usr/bin/env python3

class BankAccount(object):

    def set_attributes(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def print_attributes(self):
        slist = []
        slist.append('Name: {:s}'.format(self.name))
        slist.append('Account number: {:d}'.format(self.number))
        slist.append('Balance: {:.2f}'.format(self.balance))
        print('\n'.join(slist))

def main():

    b1 = BankAccount()
    b1.set_attributes('Jim', 12343111, 300)

    assert(b1.name == 'Jim')
    assert(b1.number == 12343111)
    assert(b1.balance == 300)

    b1.print_attributes()
    b1.deposit(100)
    b1.print_attributes()

    assert(b1.balance == 400)


if __name__ == '__main__':
    main()
