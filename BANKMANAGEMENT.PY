def generate_account_number(accounts):
    """Generate a new account number: 1001, 1002, ..."""
    if not accounts:
        return 1001
    return accounts[-1][0] + 1

def create_account(accounts):
    print("\n--- Create Account ---")
    name = input("Full name: ").strip()
    while True:
        pin = input("Choose 4-digit PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            break
        print("PIN must be exactly 4 digits.")
    acc_no = generate_account_number(accounts)
    account = [acc_no, name, pin, 0.0, []]  # balance starts at 0.0
    accounts.append(account)
    print(f"Account created. Account Number: {acc_no}\n")

def find_account(accounts, acc_no):
    """Return account list or None"""
    for acc in accounts:
        if acc[0] == acc_no:
            return acc
    return None

def login(accounts):
    print("\n--- Login ---")
    user_input = input("Account number: ").strip()
    if user_input.isdigit():
        acc_no = int(user_input)
    else:
        print("Invalid account number format.")
        return None

    acc = find_account(accounts, acc_no)
    if not acc:
        print("Account not found.")
        return None
    pin = input("Enter PIN: ").strip()
    if pin != acc[2]:
        print("Incorrect PIN.")
        return None
    print(f"Welcome, {acc[1]}!")
    return acc

def deposit(account):
    print("\n--- Deposit ---")
    user_input = input("Amount to deposit: ").strip()

    if user_input.replace('.', '', 1).isdigit():
        amt = float(user_input)
        if amt > 0:
            # Valid amount, continue processing here
            pass
        else:
            print("Amount must be positive.")
            return
    else:
        print("Invalid amount.")
        return

    account[3] += amt
    account[4].append(f"Deposit +{amt:.2f}")
    print(f"Deposited {amt:.2f}. New balance: {account[3]:.2f}")

def withdraw(account):
    print("\n--- Withdraw ---")
    user_input = input("Amount to withdraw: ").strip()

    if user_input.replace('.', '', 1).replace('-', '', 1).isdigit():
        amt = float(user_input)
        if amt > 0:
            # Valid positive amount, continue processing here
            pass
        else:
            print("Amount must be positive.")
            return
    else:
        print("Invalid amount.")
        return

    if amt > account[3]:
        print("Insufficient balance.")
        return
    account[3] -= amt
    account[4].append(f"Withdraw -{amt:.2f}")
    print(f"Withdrew {amt:.2f}. New balance: {account[3]:.2f}")

def check_balance(account):
    print("\n--- Balance ---")
    print(f"Account: {account[0]} | Name: {account[1]}")
    print(f"Balance: {account[3]:.2f}")

def view_transactions(account):
    print("\n--- Recent Transactions ---")
    if not account[4]:
        print("No transactions yet.")
        return
    # Show last 5 transactions
    for t in account[4][-5:]:
        print(t)

def account_menu(account):
    while True:
        print("\n1) Deposit  2) Withdraw  3) Check Balance  4) Transactions  5) Logout")
        choice = input("Choose: ").strip()
        if choice == "1":
            deposit(account)
        elif choice == "2":
            withdraw(account)
        elif choice == "3":
            check_balance(account)
        elif choice == "4":
            view_transactions(account)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def main():
    accounts = []  # master list of accounts
    while True:
        print("\n=== Mini Banking System ===")
        print("1) Create Account  2) Login  3) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            acc = login(accounts)
            if acc:
                account_menu(acc)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
main()