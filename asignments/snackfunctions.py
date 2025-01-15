
payment_message = """

 Collection rate  		 Amount per parcel   		 Base pay

		   		 
1.Less than 50%			  	 160			   5000
2.50% --59%				 200			   5000
3.60% --69%				 250			   5000
4.>= 70%				 500			   5000

"""
payment_option = int(input(payment_message))
 
total_amount = 0.0
	if payment_option == 1:
while True :
	ridersdelivery = float(input("Enter percentage of riders delivery: "))
	if ridersdelivery <= 0:
	total_amount = ridersdelivery * 160 + 5000

		print("Invalid input \nKindly enter again ")
	else:
		












	