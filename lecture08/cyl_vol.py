import math

def volume(r: float, h: float) -> float:
    return math.pi * r**2 * h

def main() -> None:
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    vol = volume(radius, height)
    print(f"The volume of your cylinder is {vol}")

main()