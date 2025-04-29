def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(product(1,2,3))