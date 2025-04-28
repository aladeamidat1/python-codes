total_miles = 0
total_gallons = 0
while True:
    gallons = float(input("enter gallons used: "))
    if gallons == -1:
        average = total_miles / total_gallons
        print("your total is", average)
        break
    miles = int(input("enter miles driven: "))

    total = miles / gallons

    total_miles +=miles
    total_gallons += gallons

    print("total gallons: ", total)
