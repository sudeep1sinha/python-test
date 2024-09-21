class Simple():
    def __init__(self,value):
        self.value=value

    def add_to_value(self,amount):
        self.value=self.value+amount
        print("we have added {} to ur balance".format(amount))


account=Simple(100)

print(account.value)

print(account.add_to_value(300))

print(account.value)
