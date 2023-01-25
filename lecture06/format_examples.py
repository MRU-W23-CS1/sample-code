import math

# numbers
print(f"The first 5 decimals of pi are {math.pi:.5f}")
print(f"James bond = {7:03d}")

# alignment
table_row = f"{'Left':<10}{'Right':>10}"
print(table_row)
table_row = f"{5:<10}{22:>10}"
print(table_row)
table_row = f"{5:>10}{22:>10}"
print(table_row)