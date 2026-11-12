
# ==========================================
# CASHFLOWX - MAIN ATM PROGRAM
# ==========================================

from accounts import login
from transactions import withdraw
from transactions import check_balance
from transactions import transaction_history


def main():

    print("\n================================")
    print("       WELCOME TO CASHFLOWX")
    print("================================")

    # Customer login
    card_number = login()

    if card_number is None:
        print("\nATM access denied.")
        return

    # ATM menu
    while True:

        print("\n========== ATM MENU ==========")
        print("1. Cash Withdrawal")
        print("2. Balance Enquiry")
        print("3. Last 3 Withdrawals")
        print("4. Logout")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice: ").strip()

        # Option 1: Cash Withdrawal
        if choice == "1":

            withdraw(card_number)

            input("\nPress Enter to return to ATM menu...")

        # Option 2: Balance Enquiry
        elif choice == "2":

            print("\nOption 2 selected successfully!")

            check_balance(card_number)

            input("\nPress Enter to return to ATM menu...")

        # Option 3: Last 3 Withdrawals
        elif choice == "3":

            print("\nOption 3 selected successfully!")

            transaction_history(card_number)

            input("\nPress Enter to return to ATM menu...")

        # Option 4: Logout
        elif choice == "4":

            print("\nYou have successfully logged out.")
            break

        # Option 5: Exit
        elif choice == "5":

            print("\nThank you for using CashFlowX!")
            break

        # Invalid choice
        else:

            print("\nInvalid choice!")
            print("Please enter a number between 1 and 5.")


# ==========================================
# START ATM PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
