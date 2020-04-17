

#initialazing variables
country=""
state=""
orderTotal=0
totalWithTax=0

#talking variable for  taxs
GST=0.05
HST=0.13
PST=0.06
shippingCost=0.75
importDuty =1.7
#tacking input from user
country=input("enter your country ")

if country.upper() == "INDIA" :
    state=input("enter your state")

orderTotal=float(input("enter your total order amount"))

if country.upper() == "INDIA" :
    if state.upper() == "GUJARAT" :
        orderTotal=(orderTotal+(orderTotal*GST))*shippingCost
    elif state.upper() == "MAHARASHTRA":
        orderTotal=(orderTotal+(orderTotal*HST))*shippingCost
    elif state.upper() == "PUNJAB":
        orderTotal=(orderTotal+(orderTotal*GST)+(orderTotal*PST))*shippingCost
    elif state.upper() == "TAMILNADU" :
        orderTotal=(orderTotal+(orderTotal*GST))*shippingCost
    elif state.upper() == "ANDHRAPRADESH":
        orderTotal=(orderTotal+(orderTotal*HST))*shippingCost
    elif state.upper() == "MP":
        orderTotal=(orderTotal+(orderTotal*GST)+(orderTotal*PST))*shippingCost
    elif state.upper() == "BIHAR" :
        orderTotal=(orderTotal+(orderTotal*GST))*shippingCost
    elif state.upper() == "UP":
        orderTotal=(orderTotal+(orderTotal*HST))*shippingCost
    elif state.upper() == "RAJASTHAN":
        orderTotal=(orderTotal+(orderTotal*GST)+(orderTotal*PST))*shippingCost
    elif state.upper() == "KERALA" :
        orderTotal=(orderTotal+(orderTotal*GST))*shippingCost
    elif state.upper() == "ANDHRAPRADESH":
        orderTotal=(orderTotal+(orderTotal*HST))*shippingCost
    elif state.upper() == "JK":
        orderTotal=(orderTotal+(orderTotal*GST)+(orderTotal*PST))*shippingCost
    else:
        orderTotal=(orderTotal+(orderTotal*GST)+(orderTotal*HST)+(orderTotal*PST))*shippingCost
else:
    if orderTotal <= 70000.00:
        orderTotal=orderTotal*shippingCost*importDuty
    else:
        orderTotal=orderTotal*importDuty
print("your total order value includeing tax and shipping = %0.2f Rupee" % orderTotal)

