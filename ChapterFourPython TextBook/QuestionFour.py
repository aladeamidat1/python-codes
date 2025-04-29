def fahrenheit(C):
    return (9/5) * C + 32

for degree in range(101):
    print  (f'celsius: {degree:>7}       ', f'fahrenheit: {fahrenheit(degree):>10}')