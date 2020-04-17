#importing csv file tools
import csv
filename= "guestlist.csv"
WRITE="w"
READ="r"
APPEND="a"
# asking user for how many number of guest 
noOfGuest =int(input("Enter how many guest you have invited to party?"))
file= open(filename,mode=WRITE)

for steps in range(noOfGuest):
	guestName= input("enter the name of guest::")
	guestAge= input("enter the age of guest :: ")
	file.write(guestName+","+guestAge+"\n")
file.close()
print("file created successfully")

# accessing csv file with for loop
with open("guestlist.csv",mode=READ) as mycsvFile:
    # the csv.reader() function give or return list form reading file
    guestlist1=csv.reader(mycsvFile)
    for guestdatalist in guestlist1 :
        print(':'.join(guestdatalist)) # .join() will remove [] brackets and join two worlds with ":"
