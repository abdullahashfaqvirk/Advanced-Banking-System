# Banking System

Welcome to the banking system, a tool for managing customer accounts and transactions. Customers can open accounts at the bank and perform various transactions, such as depositing and withdrawing cash or cheques. The bank can also debit accounts for fees and charges and credit them with interest.

# Classes

The following classes have been defined in this system:

* BankAccount: an abstract class representing a bank account. It has the data members account_no, balance, account_type, and opening_date, and has member functions __init__, deposit, withdraw (abstract method), credit, debit, get_balance, __str__ (abstract method), and get_account_type. It also has a class level member total_accounts.
* CurrentAccount: a child class of BankAccount representing a current account. It has no data members and has member functions __init__, debit_bank_charges, and withdraw. It overrides the withdraw and __str__ methods of BankAccount.
* SavingAccount: a child class of BankAccount representing a saving account. It has no data members and has member functions __init__, credit_daily_commission, and withdraw. It overrides the withdraw and __str__ methods of BankAccount.
* FixedDeposit: a child class of BankAccount representing a fixed deposit account. It has no data members and has member functions __init__, credit_commission, and withdraw. It overrides the withdraw and __str__ methods of BankAccount.
* SuperSavingAccount: a child class of SavingAccount representing a super saving account. It has member functions __init__, print_account, and credit_daily_commission. It also has a class level constant member MINIMUM_BALANCE initialized to 50000. It overrides the withdraw and credit_daily_commission methods of SavingAccount.

# Getting Started

To use this system, create instances of the appropriate account classes and use their member functions to perform transactions. The BankAccount class has a total_accounts class level member that keeps track of the total number of accounts opened, and the get_balance and get_account_type member functions can be used to retrieve information about an account. The print_account member function of the SuperSavingAccount class can be used to display the details of a super saving account.
