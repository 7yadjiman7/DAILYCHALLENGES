import sys

# Part I & III : BankAccount
class BankAccount:
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False          

    # Part III : authenticate sets the flag to True
    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True       

    # Part I & III : deposit
    def deposit(self, amount):
        if not self.authenticated:                          # Part III
            raise Exception("You must be authenticated to deposit.")
        if amount <= 0:                                     # Part I
            raise Exception(f"{amount} is not a positive number.")
        self.balance += amount                              
        print(f"Deposited {amount}. New balance: {self.balance}")

    # Part I & III : withdraw
    def withdraw(self, amount):
        if not self.authenticated:                          # Part III
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:                                     # Part I
            raise Exception(f"{amount} is not a positive number.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# Part II : MinimumBalanceAccount
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)   
        self.minimum_balance = minimum_balance

    # Override withdraw
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception(f"{amount} is not a positive number.")
        if self.balance - amount < self.minimum_balance:   
            raise Exception(
                f"Withdrawal denied: balance would drop below minimum ({self.minimum_balance})."
            )
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# Part IV (Bonus) : ATM
class ATM:
    def __init__(self, account_list, try_limit):
        # Validate account_list
        if not all(isinstance(acc, BankAccount) for acc in account_list):
            raise Exception("account_list must only contain BankAccount instances.")
        self.account_list = account_list

        # Validate try_limit 
        try:
            if try_limit <= 0:
                raise Exception("try_limit must be a positive number.")
            self.try_limit = try_limit
        except Exception as e:
            print(f"Invalid try_limit ({e}). Defaulting to 2.")
            self.try_limit = 2

        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n=== ATM Main Menu ===")
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid option, please try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            account.authenticate(username, password)
            if account.authenticated:
                print(f"Welcome, {account.username}!")
                self.current_tries = 0          
                self.show_account_menu(account)
                return

        # No match found
        self.current_tries += 1
        remaining = self.try_limit - self.current_tries
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            sys.exit(0)
        else:
            print(f"Invalid credentials. {remaining} attempt(s) remaining.")

    def show_account_menu(self, account):
        while True:
            print(f"\n=== Account Menu (Balance: {account.balance}) ===")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                try:
                    amount = float(input("Amount to deposit: "))
                    account.deposit(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = float(input("Amount to withdraw: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                account.authenticated = False   # déconnexion
                print("Logged out.")
                break
            else:
                print("Invalid option.")


# Tests (sans ATM qui nécessite une interaction)
if __name__ == "__main__":
    print("=== Tests BankAccount ===")
    acc = BankAccount(100, "alice", "1234")

    # Test sans authentification
    try:
        acc.deposit(50)
    except Exception as e:
        print(f"Expected error: {e}")

    # Authentification
    acc.authenticate("alice", "1234")
    acc.deposit(50)         # balance → 150
    acc.withdraw(30)        # balance → 120

    # Test montant négatif
    try:
        acc.deposit(-10)
    except Exception as e:
        print(f"Expected error: {e}")

    print("\n=== Tests MinimumBalanceAccount ===")
    min_acc = MinimumBalanceAccount(100, "bob", "5678", minimum_balance=50)
    min_acc.authenticate("bob", "5678")
    min_acc.withdraw(40)    # balance → 60, ok

    try:
        min_acc.withdraw(20)  # balance serait 40 < minimum 50 → erreur
    except Exception as e:
        print(f"Expected error: {e}")