#taking variables
guestName=" "
guestList=[]

# taking  while loop because we don't know how many guest user have invited
while guestName != "DONE" :
    guestName = input("Enter the guest name you want to enter(Enter DONE when finished)?")
    guestList.append(guestName)
    # do not know but its taking DONE in the list so putting if condition to remove done form list
    if guestName.upper() == "DONE":
        guestList.remove("DONE")
#sortin list by alphabetic order
guestList.sort()

# printing names of guestlist
for guestName in guestList :    
    print(guestName)
