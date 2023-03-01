prompt = "How much money would you like to add? "
dollars = float(input(prompt))
total = 0
while dollars > 0:
    total += dollars
    dollars = float(input(prompt))
