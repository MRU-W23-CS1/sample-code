num_a = int(input("Enter number A: ")) # ask user for an integer numberA
num_b = int(input("Enter number B: ")) # ask user for an integer numberB

if num_a > num_b:
    tmp = num_b
    num_b = num_a
    num_a = tmp
    
# if numberA > numberB
#     swap numberA and numberB

iteration = 1
possible = num_b * iteration
while abs(possible / num_a % 1) > 1e-12: # while (possible / numberA) is not an integer
    iteration += 1 #     increase iteration by 1
    possible = num_b * iteration #     possible = numberB * iteration

answer = num_b * iteration # answer = numberB * iteration
print(f"The LCM is {answer}")# display answer