investment = int(input("Enter the investment: $"))

for years in range(1, 30):
    a = investment *( 1 + 0.07) ** years
    print(a)

