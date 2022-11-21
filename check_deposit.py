from transaction import *
from currentaccount import *

class CheckDeposit(Transaction):
    def __init__(self, amount, check_no, bank, obj, transaction_type='Check Deposit'):
        super().__init__(amount, transaction_type)
        self.__check_no = check_no
        self.__bank = bank
        obj.credit(amount)
    
    def debit(self):
        pass

    def credit(self):
        pass

    def __str__(self):
        return super().__str__() + f"\t{self.__check_no}\t{self.__bank}"


