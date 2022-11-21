from abc import ABC, abstractmethod
from random import randint
from datetime import datetime
from date import *


class BankAccount(ABC):
    total_accounts = 0

    def __init__(self, opening_balance, account_type):
        BankAccount.total_accounts += 1
        self.__account_no = BankAccount.total_accounts
        self.__balance = opening_balance
        self.__account_type = account_type
        self.__status = 'active'
        self.__datetime = str(datetime.now())
        self.__opening_date = Date(self.__datetime[8:10], self.__datetime[5:7], self.__datetime[:4])
        print(f"Account no: {self.__account_no} of {self.__account_type} type is opened with balance: {self.__balance}")

    def deposit(self, amount):
        if self.__status == 'active':
            self.__balance += amount
            print(f"{amount} is deposit into Account no: {self.__account_no}")
        else:
            print(f"Account: {self.__account_no} is terminated - Deposit")

    @abstractmethod
    def withdraw(self, amount):
        if self.__status == 'active':
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"{amount} is withdraw from Account no: {self.__account_no}")
            else:
                print(f"{self.__balance - amount} money is short for withdrawal from Account no: {self.__account_no}")
        else:
            print(f"Account: {self.__account_no} is terminated - Withdraw")

    def credit(self, amount):
        if self.__status == 'active':
            self.__balance += amount
            print(f"{amount} is credited into Account no: {self.__account_no}")
        else:
            print(f"Account: {self.__account_no} is terminated - Credit")

    def debit(self, amount):
        if self.__status == 'active':
            self.__balance -= amount
            print(f"{amount} is debited into Account no: {self.__account_no}")
        else:
            print(f"Account: {self.__account_no} is terminated - Debit")

    def get_balance(self):
        if self.__status == 'active':
            return self.__balance
        else:
            print(f"Account: {self.__account_no} is terminated - Get Balance")
    
    def set_balance(self, balance):
        if self.__status == 'active':
            self.__balance = balance
        else:
            print(f"Account: {self.__account_no} is terminated - Set Balance")
    
    def check_balance(self, amount):
        if type(amount) == type(None):
            return randint(5000, 5000000)
        return amount

    @abstractmethod
    def __str__(self):
        if self.__status == 'active':
            return f"{self.__account_no}\t{(self.__account_type).ljust(15)}\t{round(self.__balance, 2)}"
        return f"{self.__account_no}\t{self.__status}"


    def print_account(self):
        print(f"{str(self.__account_no).ljust(5)}{(self.__account_type).ljust(15)}{str(round(self.__balance, 2)).ljust(10)}{str(self.__opening_date).rjust(15)}")

    def terminate(self):
        self.__status = 'terminate'

    def get_status(self):
        return self.__status

    def get_account_type(self):
        return self.__account_type

    def get_total_accounts(self):
        return BankAccount.total_accounts
