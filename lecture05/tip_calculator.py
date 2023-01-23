# Constants
TIP_PERCENT = 0.02

# Inputs
num_employees = 6
total_sales = 8000

# Processing
total_tips = total_sales * TIP_PERCENT
tips_each = total_tips / num_employees

# Output
print("Everyone takes home $", tips_each, sep="")