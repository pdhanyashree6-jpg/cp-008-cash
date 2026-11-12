
# ==========================================
# CASHFLOWX - CUSTOMER ACCOUNT DATA
# ==========================================

# Daily withdrawal limit for each customer
DAILY_LIMIT = 10000

# Customer account details
accounts = {

    "123456789": {
        "pin": "1234",
        "balance": 20000,
        "blocked": False,
        "wrong_attempts": 0,
        "daily_withdrawn": 0,
        "withdrawals": []
    },

    "987654321": {
        "pin": "5678",
        "balance": 15000,
        "blocked": False,
        "wrong_attempts": 0,
        "daily_withdrawn": 0,
        "withdrawals": []
    },

    "456789123": {
        "pin": "1111",
        "balance": 25000,
        "blocked": False,
        "wrong_attempts": 0,
        "daily_withdrawn": 0,
        "withdrawals": []
    }
}


# Function to display customer accounts
def display_accounts():

    print("\n===== CUSTOMER ACCOUNT DETAILS =====")

    for card_number, details in accounts.items():

        print("\nCard Number:", card_number)
        print("Balance: Rs.", details["balance"])

        if details["blocked"]:
            print("Card Status: Blocked")
        else:
            print("Card Status: Active")


# Function to get a customer's account
def get_account(card_number):

    return accounts.get(card_number)

# LOGIN SECURITY FUNCTION

def login():

    card_number = input("Enter your card number: ")

    if card_number not in accounts:
        print("Invalid card number!")
        return None

    account = accounts[card_number]

    if account["blocked"]:
        print("Your card is blocked!")
        return None

    for attempt in range(3):

        pin = input("Enter your PIN: ")

        if pin == account["pin"]:

            print("Login successful!")
            account["wrong_attempts"] = 0
            return card_number

        else:

            account["wrong_attempts"] += 1

            print("Incorrect PIN!")

            if attempt < 2:
                print("Attempts remaining:", 2 - attempt)

    account["blocked"] = True

    print("Your card has been blocked!")

    return None


