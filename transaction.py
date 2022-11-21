from datetime import datetime
from abc import ABC, abstractmethod
from date import *

class Transaction(ABC):
    total_transaction = 0

    def __init__(self, amount, transaction_type):
        self.__datetime = str(datetime.now())
        self.__trans_date = Date(self.__datetime[8:10], self.__datetime[5:7], self.__datetime[:4])
        self.__amount = amount
        Transaction.total_transaction += 1
        self.__trans_number = Transaction.total_transaction
        self.__credit_debit = transaction_type

    @abstractmethod
    def debit(self):
        pass

    @abstractmethod
    def credit(self):
        pass

    @abstractmethod
    def __str__(self):
        return f"{self.__trans_number}\t{self.__trans_date}\t{self.__amount}\t{self.__credit_debit}"
