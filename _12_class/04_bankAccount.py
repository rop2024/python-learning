# Bank Account: Create a BankAccount
# class with attributes like account holder name,
# balance, and account number. Add methods for depositing,
# withdrawing, and checking the balance. Implement error
# handling to prevent overdrafts.


class BankAccount:
    accountCounter = 0

    def __init__(self, name, balance = 0):
        self.__name = name
        self.__balance = balance
        self.__number = f'{BankAccount.accountCounter:003}'
        BankAccount.accountCounter += 1

    def __str__(self):
        return f"Account holder name : {self.__name}\nAccount number: {self.__number}\nBalance: {self.__balance}"

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print("Money deposited.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amt):
        if amt > 0:
            if self.__balance >= amt:
                self.__balance -= amt
                print("Money withdrawn.")
            else:
                print("Not enough funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

    def get_account(self):
        return self.__number

def main():
    bank()

def bank():
    print("Welcome to Xyz Bank")
    new_account = None
    print("-----")
    print("Here are choices...")
    print("1. create account[C,c,create]\n2. withdraw[W,w,withdraw]\n3.deposit[D,d,deposit]\n4.Account info[I,i,info]")

    loop = True
    while loop:
        choice = input("What would you like to do: ").lower()

        if choice in ['c', 'create']:
            name = input("Enter name: ")
            bal = int(input("Enter initial balance: "))

            new_account = BankAccount(name, bal)
            print("Account has been created")
            print(new_account)

        elif choice in ['w', 'withdraw']:
            if new_account:
                amount = int(input("Enter amount to withdraw: "))
                new_account.withdraw(amount)
            else:
                print("Create account first")

        elif choice in ['d', 'deposit']:
            if new_account:
                amount = int(input("Enter amount to deposit: "))
                new_account.deposit(amount)
            else:
                print("Create account first")

        elif choice in ['i', 'info']:
            if new_account:
                print(new_account)
            else:
                print("Create account first")

        else:
            print("Wrong choice !! No action")

        choice2 = input("Do you want to quit?").lower()

        if choice2 in ['yes', 'y']:
            loop = False


if __name__ == "__main__":
    main()