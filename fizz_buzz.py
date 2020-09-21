
# Start with some pseudo-code!
# Define a range from 0 to 100
# write fuzz if a number is divided by 3
# write buzz if a number i divided by 5
# write fizzbuzz if a number is divided by 3 and 5

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0:
        print("fizz")
    else:
        print(n)


