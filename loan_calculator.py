# Initialize variabls
monthlypayment = 0
loanamount =0
interrestrate =0
numberofyears =0 
numberofpayment =0 

#taking inpur from the user
str_loanamount=input("how much amount of loan you want to  take \n ")
str_interestrate=input("how much interest you want to pay\n")
str_numberofyears=input("for how many years you want the lone\n")

#converting strings to float
loanamount=float(str_loanamount)
interrestrate=float(str_interestrate)
numberofyears=float(str_numberofyears)

#number of payments
numberofpayment = 12 * numberofyears

#calculating mortgage
# m=l[i(1+i)n]/[(1+i)n-1]
monthlypayment = loanamount * interrestrate * (1+interrestrate) * numberofpayment /((1+interrestrate)*numberofpayment-1)

#outpur
print(" your monthly payment  will be =",monthlypayment)