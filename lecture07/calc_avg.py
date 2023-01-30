def average(num1: float, num2: float) -> None:
    avg = (num1 + num2) / 2
    print(f"The average of {num1} and {num2} is {avg}")

def main() -> None:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    average(x, y)
    average(2 * x, 3 * y)

main()