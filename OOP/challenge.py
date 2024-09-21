class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,deposit):
        self.balance=self.balance + deposit
        print("{} has been deposited in ur account".format(deposit))

    def withdraw(self,withdraw):
        if self.balance > withdraw:
            self.balance=self.balance - withdraw
            print("{} has been withdrawn from ue account".format(withdraw))
        else:
            print("sorry , funds unavailable")

    def __str__(self):
        return f"owner: {self.owner} \nbalance: {self.balance}"





bank=Account(owner='sudeep',balance=1000)

print(bank.owner)

print(bank.balance)

print(bank.deposit(100))
print(bank.withdraw(4000))
print(bank)




    
