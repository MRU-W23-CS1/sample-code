from math import tan, pi
# could also just import math and then access math.tan

def apothem_area(n: int, a: float) -> float:
    """
    Calculates the area of a polygon with 
    n sides and apothem length a.
    """
    area = n * a * 2 * tan(pi / n)
    return area

def main() -> None:
    n_sides = int(input("Enter the number of sides: "))
    a_length = float(input("Enter the length of the apothem: "))
    print(apothem_area(n_sides, a_length))

main()