from transaction import *
from currentaccount import *

class CheckWithdrawal(Transaction):
    def __init__(self, amount, check_no, title, bank, obj, transaction_type='Check Withdrawal'):
        super().__init__(amount, transaction_type)
        self.__check_no = check_no
        self.__title = title
        self.__bank = bank
        obj.debit(amount)

    def debit(self):
        pass

    def credit(self):
        pass

    def __str__(self):
        return super().__str__() + f"\t{self.__check_no}\t{self.__title}\t{self.__bank}"

