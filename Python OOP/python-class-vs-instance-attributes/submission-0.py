class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_counts = 0
    total_balance = 0
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_counts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format

print(f"{account1.name}'s balance: ${account1.balance}")
print(f"{account2.name}'s balance: ${account2.balance}")
print(f"Total Accounts: {BankAccount.total_counts}")
print(f"Total Balance: ${BankAccount.total_balance}")

