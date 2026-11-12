
# ==========================================
# CASHFLOWX - TRANSACTION MANAGEMENT
# ==========================================

from accounts import accounts, DAILY_LIMIT
from atm import find_notes, dispense_cash


# ==========================================
# CUSTOMER CASH WITHDRAWAL
# ==========================================

def withdraw(card_number):

    account = accounts.get(card_number)

    if account is None:
        print("Customer account not found!")
        return

    print("\n===== CASH WITHDRAWAL =====")

    # Get withdrawal amount
    try:
        amount = int(input("Enter withdrawal amount: "))
    except ValueError:
        print("Invalid input! Enter numbers only.")
        return

    # Check valid amount
    if amount <= 0 or amount % 100 != 0:
        print("Enter a valid amount in multiples of Rs. 100.")
        return

    # Check account balance
    if amount > account["balance"]:
        print("Insufficient account balance!")
        return

    # Check daily withdrawal limit
    if account["daily_withdrawn"] + amount > DAILY_LIMIT:
        print("Daily withdrawal limit exceeded!")
        print("Daily limit: Rs.", DAILY_LIMIT)
        return

    # Check whether ATM can dispense the amount
    notes = find_notes(amount)

    if notes is None:
        print("ATM does not have sufficient notes.")
        return

    # Dispense cash
    success = dispense_cash(amount)

    if not success:
        print("Transaction failed!")
        return

    # Update customer account
    account["balance"] -= amount

    # Update daily withdrawal amount
    account["daily_withdrawn"] += amount

    # Save successful transaction
    account["withdrawals"].append(amount)

    print("\n===== TRANSACTION SUCCESSFUL =====")
    print("Withdrawn Amount: Rs.", amount)
    print("Remaining Balance: Rs.", account["balance"])
    print("Today's Total Withdrawal: Rs.",
          account["daily_withdrawn"])
    print("Remaining Daily Limit: Rs.",
          DAILY_LIMIT - account["daily_withdrawn"])


# ==========================================
# BALANCE ENQUIRY
# ==========================================

def check_balance(card_number):

    account = accounts.get(card_number)

    if account is None:
        print("Customer account not found!")
        return

    print("\n===== BALANCE ENQUIRY =====")
    print("Available Balance: Rs.", account["balance"])


# ==========================================
# LAST 3 WITHDRAWALS
# ==========================================

def transaction_history(card_number):

    account = accounts.get(card_number)

    if account is None:
        print("Customer account not found!")
        return

    print("\n===== LAST 3 WITHDRAWALS =====")

    withdrawals = account["withdrawals"]

    if len(withdrawals) == 0:
        print("No withdrawal transactions found.")
        return

    # Display the latest 3 withdrawals
    for amount in reversed(withdrawals[-3:]):

        print("Withdrawn Amount: Rs.", amount)

