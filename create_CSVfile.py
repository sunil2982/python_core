filename = "guest.csv"
WRITE ="w"
APPEND ="a"
EDIT ="w+"
guestName=""
guestAge = 0
noOfGuest = int(input("enter how many guest you wnat to invite"))
file = open(filename,mode=WRITE)
for steps in range(noOfGuest)  :
    guestName =input("Enter name of Guest:: ")
    guestAge = input("enter Age of Guest::")
    file.write(guestName + ","+ guestAge+"\n")
    
file.close()   
print("file created successfully")