from transaction import *
from currentaccount import *

class CashDeposit(Transaction):
    def __init__(self, amount, obj, transaction_type='Cash Deposit'):
        super().__init__(amount, transaction_type)
        obj.deposit(amount)
    
    def debit(self):
        pass

    def credit(self):
        pass

    def __str__(self):
        return super().__str__()

