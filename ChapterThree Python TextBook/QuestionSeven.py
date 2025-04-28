value = int(input('Enter a five digit number: '))
divisor = 10000
for num in range(5):
    digit = value // divisor
    print(digit, end=' ')
    value = value % divisor
    divisor = divisor // 10


