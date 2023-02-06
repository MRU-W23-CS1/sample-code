TIP_PERCENT = 0.02
# Don't do the next two lines! Global variables = bad ish
sales = float(input("Enter the total sales: "))
num_employees = int(input("Enter the number of employees: "))

def calc_tipout(sales: float, num_employees: int) -> float:
    return sales * TIP_PERCENT / num_employees

def main() -> None:
    tips = calc_tipout(100, num_employees)
    print(f"At {TIP_PERCENT:.1%} tipout, each employee gets ${tips:.2f}")

main()