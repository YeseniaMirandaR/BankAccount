#Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    allAccounts = []

    def __init__ (self, interestRate, balance):
        self.interestRate = interestRate
        self.balance = balance
        BankAccount.allAccounts.append(self)

    #Add a deposit method to the BankAccount class
    def deposit (self, amount):
        self.balance += amount
        return self

    #Add a withdraw method to the BankAccount class
    def withdraw (self, amount):
        if (self.balance - amount)>= 0:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: charging a $5 fee")
        return self

    #Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    #Add a yield_interest method to the BankAccount class
    def yield_interest(self): #if balance is positive, it increases the account balance by the current balance*the interest rate
        if self.balance > 0:
            self.balance += (self.balance*self.interestRate)
        return self

    #NINJA BONUS: use a classmethod to print all instances of a Bank Account's info  #classmethod uses cls instead of self
    @classmethod
    def printallAccountsInfo(cls):
        for account in cls.allAccounts:
            account.display_account_info()

    #Create 2 accounts	
    #To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
    #To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

#(interest rate, amount)
User1Account = BankAccount(.01, 2000)  
User2Account = BankAccount(.03, 1500)

User1Account.deposit(40000).deposit(20000).deposit(10000).withdraw(2500).yield_interest().display_account_info()
User2Account.deposit(1500).deposit(10000).withdraw(1000).withdraw(750).withdraw(800).withdraw(50).yield_interest().display_account_info()


BankAccount.printallAccountsInfo()
