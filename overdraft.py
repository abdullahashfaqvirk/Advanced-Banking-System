from currentaccount import *

class OverdraftAccount(CurrentAccount):
    MINIMUM_BALANCE = -50000
    
    def __init__(self, balance, account_type='OD'):
        super().__init__(balance, account_type)

    def withdraw(self, amount):
        balance = self.get_balance()
        check_balance = self.check_balance(balance)
        if self.get_status == 'active':
            if check_balance - amount >= OverdraftAccount.MINIMUM_BALANCE:
                self.set_balance(check_balance - amount)
            else:
                print("Conditions don't satisfied for withdrawal.")
        else:
            print("Account is terminated - Withdraw OverdraftAccount")

    def debit_bank_charges(self):
        self.debit(500)
    
    def __str__(self):
        return super().__str__()

