"""
  LAB 03
  PROGRAMMING PROBLEM 03

  The str method of the Bank class returns a string containing the accounts in random order. Design and
  implement a change that causes the accounts to be placed in the string by order of name. (Hint: You will
  also have to define some methods in the SavingsAccount class.)
"""
class SavingsAccount:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}: ${self.balance:.2f}"

    def __lt__(self, other):
        #Comparing the account for sorting by name
        return self.name < other.name


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        #Addition of a new account
        self.accounts.append(account)

    def __str__(self):
        #Alphabetical sorting of accounts to display
        sorted_accounts = sorted(self.accounts)
        return "\n".join(str(account) for account in sorted_accounts)


#Sample use of the code
if __name__ == "__main__":
    bank = Bank()
    bank.add_account(SavingsAccount("Alice", 1500))
    bank.add_account(SavingsAccount("Charlie", 1200))
    bank.add_account(SavingsAccount("Bob", 1800))

    print("Bank Accounts:")
    print(bank)
