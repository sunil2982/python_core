# calculate shipping charges for a shopper
# ask user to enter the total amount of their purchase
# if the total is under $50 add $10, otherwise shipping is free
# tell the user their final total including shipping coast and format the number 
# so it looks like a monetary value


#making variables
total_cost=float(input("please enter your total amount"))
# shipping =False
if total_cost <= 50.00:
    # shipping = True
    total_cost = total_cost + 10  # 10 is shipping coast
    print("your total bill is iteam + shippint",total_cost),"$"
else:
    print("your total bill is =",total_cost,"$")


