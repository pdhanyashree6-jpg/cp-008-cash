
# CashFlowX – ATM Cash Dispensing and Security Simulator

## Project Overview

CashFlowX is a Python-based ATM Cash Dispensing and Security Simulator developed as part of the CP-008 project under the Banking and FinTech domain.

The project simulates the basic operations of an ATM system, including secure customer login, cash withdrawal, balance enquiry, transaction history, and ATM cash inventory management.

It aims to demonstrate how ATM transactions and basic banking security operations work using Python programming.

## Features

- **Secure Customer Login:** Customers log in using their card number and PIN.
- **Login Security:** Automatically blocks a card after three incorrect PIN attempts.
- **Cash Withdrawal:** Allows customers to withdraw money from their accounts.
- **Minimum Note Dispensing:** Uses ₹500, ₹200, and ₹100 denominations to dispense cash using the minimum possible number of notes.
- **ATM Cash Inventory:** Tracks the available number of currency notes in the ATM.
- **Daily Withdrawal Limit:** Restricts customers from withdrawing more than ₹10,000 per day.
- **Balance Enquiry:** Displays the customer's available account balance.
- **Transaction History:** Displays the last three successful withdrawals.

## Technologies Used

- Programming Language: Python
- Development Environment: Visual Studio Code
- Version Control: Git and GitHub

## Project Structure

```text
cp-008-cash/
│
├── main.py
├── accounts.py
├── atm.py
├── transactions.py
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `main.py` | Runs the main ATM menu and connects all modules. |
| `accounts.py` | Stores customer account details and handles login security. |
| `atm.py` | Manages ATM cash inventory and currency note calculations. |
| `transactions.py` | Handles withdrawals, balance enquiry, and transaction history. |
| `README.md` | Contains project documentation. |

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open the Project Folder

```bash
cd cp-008-cash
```

### Step 3: Run the Application

```bash
python main.py
```

## Sample Login Credentials

The project includes sample customer accounts for testing.

| Card Number | PIN |
|---|---|
| 123456789 | 1234 |
| 987654321 | 5678 |
| 456789123 | 1111 |

**Note:** These are demonstration credentials for the simulator, not real banking credentials.

## Sample ATM Operations

1. Log in using a valid card number and PIN.
2. Select Cash Withdrawal to withdraw money.
3. Select Balance Enquiry to check the remaining balance.
4. Select Last 3 Withdrawals to view recent transactions.
5. Select Logout to end the session.

## Future Enhancements

- Admin login and authentication.
- ATM cash refill functionality.
- Persistent storage of customer and transaction data.
- Automatic daily withdrawal limit reset.
- Transaction receipt generation.
- Improved PIN security using password hashing.

## Disclaimer

CashFlowX is an educational project developed for learning and demonstration purposes. It is not connected to any real banking system and should not be used for actual financial transactions.

## Author

Developed as part of the CP-008 Banking and FinTech project.