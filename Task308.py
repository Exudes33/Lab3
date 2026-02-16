class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Funds"

a = input().split()
initial_balance = int(a[0])
withdraw_amount = int(a[1])


my_account = Account("User", initial_balance)

print(my_account.withdraw(withdraw_amount))
