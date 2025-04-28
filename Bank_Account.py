
class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0.00
        self.transaction = []

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"{self.name} deposited {amount} sucessfully")

    def withdraw(self,amount):
        if amount > self.balance:
            print("withdraw not sucessful")
        elif amount < 0:
            print ("withdraw sucessful")

    #def show transaction()




