from savingaccount import *

class SuperSavingAccount(SavingAccount):
    MINIMUM_BALANCE = 50000

    def __init__(self, balance, account_type='S_SAVING'):
        super().__init__(balance, account_type)

    def withdraw(self, amount):
        balance = self.get_balance()
        check_balance = self.check_balance(balance)
        if self.get_status == 'active':
            if check_balance >= amount + SuperSavingAccount.MINIMUM_BALANCE:
                self.set_balance(check_balance - amount)
            else:
                print("Conditions don't satisfied for withdrawal.")
        else:
            print("Account is terminated - Withdraw SuperSavingAccount")

    def print_account(self):
        super().print_account()
        print(f"{SuperSavingAccount.MINIMUM_BALANCE} minimum balance is required here!".rjust(44))

    def credit_daily_commision(self):
        balance = self.get_balance()
        commision = round(self.check_balance(balance) * 0.01, 2)
        self.credit(commision)
    
    def __str__(self):
        return super().__str__()

