n = int(input("Enter a non-negative integer: "))

n_factorial = 1
value = n
while value > 1:
    n_factorial *= value
    value -= 1

print("The factorial of", n, "is", n_factorial)