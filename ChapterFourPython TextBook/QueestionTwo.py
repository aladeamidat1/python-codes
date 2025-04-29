def average(req,*args):
    numbers = (req,) + args
    return sum(numbers) / len(numbers)