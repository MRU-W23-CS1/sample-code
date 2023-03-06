def enter_grades() -> float:
    """
    Prompts the user to repeatedly enter grades.
    Stops when -1 encountered.
    """
    prompt = "Enter a grade, stop on -1: "
    grade = float(input(prompt))
    total = 0
    n_grades = 0
    while grade > 0:
        total += grade
        n_grades += 1
        print(f"The running average is {total / n_grades}")
        grade = float(input(prompt))

    return total / n_grades
    
def main() -> None:
    print(f"Final Average: {enter_grades()}")

main()