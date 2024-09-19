class Account():
    def __init__(self, number, balance, password):
        self.number = number
        self.balance = balance
        self.password = password

    def deposit(self, amountTodeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amountTodeposit < 0:
            print("You can't deposit a negative amount")
            return None
        self.balance += amountTodeposit
        return self.balance
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Incorrect password")
            return None
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None
        if amountToWithdraw > self.balance:
            print("You cannot withdraw more than your balance")
            return None
        self.balance -= amountToWithdraw
        return self.balance
    
    def show(self):
        print(self.number)
        print(self.balance)

def main():
    alice = Account("0001", 1000.50, "BSU")
    bob = Account("0002", 100, "iu")
    bob.deposit(50, "BSU") #This is us depositing and putting the amount and password so we are able to add money and comfirm it is us
    bob.show()
    alice.show()
main()