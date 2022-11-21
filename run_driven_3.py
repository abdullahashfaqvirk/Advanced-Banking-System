"""THIS IS THE MENU-DRIVEN CODE FOR CHECKING SOME OF THE CLASSES FUNCTIONALITIES"""
"""ALL CLASSES FUNCTIONALITIES ARE NOT CHECKED"""

from cash_deposit import *
from cash_withdraw import *
from check_deposit import *
from check_withdraw import *
from bankaccount import *
from currentaccount import *
from savingaccount import *
from fixeddeposit import *
from supersavingaccount import *
from overdraft import *
from random import *

CHECK_N0 = 'M034'
BANK = 'FCIT'
TITLE = 'BSDS'

def user_menu():
    print(f"<<<<< Choose Account Type >>>>>\n{'-'*31}")
    print("1. Current Account\n2. Saving Account\n3. Fixed Deposit\n4. Super Saving Account\n5. Draft Account\n")
    num = int(input("Enter Option: "))
    opening_balance = int(input("Enter Opening Balance: "))
    if num == 1: obj = CurrentAccount(opening_balance)
    elif num == 2: obj = SavingAccount(opening_balance)
    elif num == 3: obj = FixedDeposit(opening_balance)
    elif num == 4: obj = SuperSavingAccount(opening_balance)
    else: obj = OverdraftAccount(opening_balance)
    return obj

def universal_properties(obj):
    while True:
        print("\nChoose an Option:\n1. Cash Deposit\n2. Cash Withdrawal\n3. Check Deposit\n4. Check Withdrawal\n5. Get Balance\n6. Get Account Details\n7. Quite\n")
        num = int(input("Enter Option: "))
        if num >= 1 and num <= 4: opening_amount = int(input('Enter Amount: '))
        if num == 1: cd = CashDeposit(opening_amount, obj); print(cd)
        elif num == 2: cw = CashWithdraw(opening_amount, CHECK_N0, obj); print(cw)
        elif num == 3: cd = CheckDeposit(opening_amount, CHECK_N0, BANK, obj); print(cd)
        elif num == 4: cw = CheckWithdrawal(opening_amount, CHECK_N0, TITLE, BANK, obj); print(cw)
        elif num == 5: print(obj.get_balance())
        elif num == 6: obj.print_account()
        else: print("\nThank You For Using!!!\n"); break


def main():
    user_menu_tasks = user_menu()
    universal_properties(user_menu_tasks)

main()
