print(f'{"numbers":>6} {"square":>6} {"cube":>6}')
for numbers in  range(0,6):
    square = numbers * numbers
    cube = numbers * numbers * numbers

    print(f'{numbers:>6} {square:>6} {cube:>6}')
