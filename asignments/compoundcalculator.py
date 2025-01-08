import math
while (True):
	investment = float(input("Enter initial investment: "))
	if investment <= 0:
		print("Invalid Input \nKindly enter again ")
	else:
		break

while (True):
	years = int(input("Enter length of time in years: "))
	if years <= 0:
		print("Invalid Input \nKindly enter again ")
	else:
		break

while True:
	estimatedInterest = float(input("Enter estimated interest rate: "))
	if estimatedInterest <= 0:
		print("Invalid Input \nKindly enter again ")
	else:
		break

annual = 1
semi_annual = 2
quarterly = 4
monthly = 12
daily = 365

duration = """

Select Compound Frequency
1. Annually
2. Semiannually
3. Quarterly
4. Monthly
5. Daily

"""
compound_frequency = int(input(duration))

rate = estimatedInterest / 100
total_amount = 0.0

if compound_frequency == 1:
   total_amount = investment * (1 + (rate / annual)) ** (annual * years) 
elif compound_frequency == 2:
   total_amount = investment **(1 + rate / semi_annual * semi_annual * years)
elif compound_frequency == 3:
   total_amount = investment ** (1 + rate / quarterly * quarterly * years)
elif compound_frequency == 4:
   total_amount = investment ** (1 + rate / monthly * monthly * years)
elif compound_frequency == 5:
   total_amount = investment ** (1 + rate / daily * daily * years)


print(f"Total amount: {total_amount:.2f}")
