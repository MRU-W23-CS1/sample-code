# Casting directly to int
an_int = int(input("Enter an integer: "))
print("an_int * 5 =", an_int * 5)

# Indirect casting
a_string_int = input("Enter an integer: ")
print("a_string_int * 5 =", a_string_int * 5)
an_int = int(a_string_int)
print("an_int * 5 =", an_int * 5)

# works with float too
a_float = float(input("Enter a float: "))
print(a_float)