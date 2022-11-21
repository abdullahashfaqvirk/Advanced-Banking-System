from bankaccount import *

class FixedDeposit(BankAccount):
    def __init__(self, opening_balance, account_type='FIXED'):
        super().__init__(opening_balance, account_type)

    def credit_commission(self):
        balance = self.get_balance()
        commision = round(self.check_balance(balance) * 0.12, 2)
        self.credit(commision)

    def withdraw(self, amount):
        print("This is a fixed deposit account, widthdrawal not allowed")
    
    def __str__(self):
        return super().__str__()
