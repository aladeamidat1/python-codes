passes = 0
faliures = 0

for number in range(10):
    value = int(input('Enter any number: '))
    if value == 1:
        passes += 1
    elif value == 2:
        passes += 1
    else:
        faliures += 1

print("You passed", passes, "passes")
print("You failed", faliures, "failures")

