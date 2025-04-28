largest1 = 0
largest2 = 0
for number in range(10):
    value = int(input("Enter a number: "))
    if value > largest1:
        largest2 = largest1
        largest1 = value
    elif value > largest2:
        largest2 = value


print(largest1)
print(largest2)

