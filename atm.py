
# ==========================================
# CASHFLOWX - ATM CASH INVENTORY
# ==========================================

# Available currency notes in the ATM

atm_inventory = {
    500: 10,
    200: 20,
    100: 30
}



# ==========================================
# FIND MINIMUM NUMBER OF NOTES
# ==========================================

def find_notes(amount):

    best_combination = None
    minimum_notes = float("inf")

    # Maximum available ₹500 notes
    max_500 = min(amount // 500, atm_inventory[500])

    for n500 in range(max_500 + 1):

        remaining = amount - (n500 * 500)

        # Maximum available ₹200 notes
        max_200 = min(remaining // 200, atm_inventory[200])

        for n200 in range(max_200 + 1):

            remaining_amount = remaining - (n200 * 200)

            # Check whether ₹100 notes can complete the amount
            if remaining_amount % 100 != 0:
                continue

            n100 = remaining_amount // 100

            # Check available ₹100 notes
            if n100 > atm_inventory[100]:
                continue

            # Calculate total number of notes
            total_notes = n500 + n200 + n100

            # Find the combination with minimum notes
            if total_notes < minimum_notes:

                minimum_notes = total_notes

                best_combination = {
                    500: n500,
                    200: n200,
                    100: n100
                }

    return best_combination



# ==========================================
# DISPENSE CASH
# ==========================================

def dispense_cash(amount):

    notes = find_notes(amount)

    if notes is None:

        print("\nSorry! ATM cannot dispense this amount.")
        return False

    # Update ATM inventory
    for denomination, count in notes.items():

        atm_inventory[denomination] -= count

    print("\nCash dispensed successfully!")

    print("\nCurrency details:")

    for denomination, count in notes.items():

        if count > 0:

            print("Rs.", denomination, "x", count)

    return True



# ==========================================
# DISPLAY ATM INVENTORY
# ==========================================

def display_inventory():

    print("\n===== ATM CASH INVENTORY =====")

    for denomination, count in atm_inventory.items():

        print("Rs.", denomination, "notes:", count)

