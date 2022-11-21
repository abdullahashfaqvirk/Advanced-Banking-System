from bankaccount import *

class CurrentAccount(BankAccount):
    def __init__(self, opening_balance, account_type='CURRENT'):
        super().__init__(opening_balance, account_type)

    def debit_bank_charges(self):
        self.debit(100)
    
    def withdraw(self, amount):
        return super().withdraw(amount)
    
    def __str__(self):
        return super().__str__()

