from transaction import *
from currentaccount import *

class CashWithdraw(Transaction):
    def __init__(self, amount, check_no, obj, transaction_type='Cash Withdrawal'):
        super().__init__(amount, transaction_type)
        self.__check_no = check_no
        obj.withdraw(amount)
    
    def debit(self):
        pass

    def credit(self):
        pass

    def __str__(self):
        return super().__str__() + f"\t{self.__check_no}"

