# result = 10
result = -1
total = float(input("Please enter the total: "))
if total > 100:
    print("Total is", total)
    result = 25
elif total < 20:
    print("Total is", total)
    result = 80

print("Result is", result)