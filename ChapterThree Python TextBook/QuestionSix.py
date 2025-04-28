total = 0
product = 1
average = 0
smallest = 0
largest = 0
for number in range(4):
    value = int(input('Enter any number: '))
    if number == 0:
        smallest = value
    elif value < smallest:
        smallest = value

    if value > largest:
        largest = value
    total += value
    product *= value
average = total / 4


print(total)
print(product)
print(average)
print(smallest)
print(largest)
