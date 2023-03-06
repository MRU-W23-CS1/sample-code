TARGET = 500
INTEREST = 0.02

balance = 100
years = 0 # this is my accumulator!
while balance < TARGET:
    print(f"Balance is ${balance:.2f}")
    balance += 50
    years += 1
    balance *= 1 + INTEREST

print(f"It took {years} years to reach {TARGET}")