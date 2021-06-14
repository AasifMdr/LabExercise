'''
Price of a house is $1M.
If buyer has good credit,
they need to put down 10%
otherwise
they need to put down 20%.
Print the down payment.
'''

price_house = 1000000
answer = input("Do you have good credit yes or no?: ")
if answer == "yes" or "Yes":
    print(f"You Payed 10% that is {(10/100) * price_house}.")
elif answer == "no" or "No":
    print(f"You Payed 10% that is {(20/100) * price_house}.")
else:
    print("Please enter yes or no.")