DISCOUNT_THRESHOLD = 50
DISCOUNT_PERCENT = 0.85
GST = 0.05

def calc_total(purchase: float, is_first_tuesday: bool) -> float:
    """
    Calculates the total based on discount eligibility
    """
    if purchase > DISCOUNT_THRESHOLD and is_first_tuesday:
        purchase = purchase * DISCOUNT_PERCENT
        print("You're eligible for a discount!")
    else:
        print("Sorry, no discount today.")
    
    total = purchase * (1 + GST)
    return total

def main() -> None:
    amount = float(input("How much is your purchase? "))
    print(f"First Tuesday: With GST, you owe ${calc_total(amount, True):.2f}")
    print(f"Different day: With GST, you owe ${calc_total(amount, False):.2f}")

main()