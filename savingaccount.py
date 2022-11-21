from bankaccount import *

class SavingAccount(BankAccount):
    def __init__(self, opening_balance, account_type='SAVING'):
        super().__init__(opening_balance, account_type)

    def credit_daily_commision(self):
        balance = self.get_balance()
        commision = round(self.check_balance(balance) * 0.008, 2)
        self.credit(commision)

    def withdraw(self, amount):
        return super().withdraw(amount)
    
    def __str__(self):
        return super().__str__()
