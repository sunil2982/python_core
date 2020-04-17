# the datetime class allows us to get the current date and time
import datetime

#today() is a function that returns todays date
currentdate=datetime.date.today()
print("today date is =",currentdate)
# print("this is year ",currentdate.year)
# print("this is month ",currentdate.month)
# print("this is date ",currentdate.day)

# #strftime allows you to specify the date format
# print(currentdate.strftime("%d %b %Y"))
# print(currentdate.strftime("%d %b %y"))
print(currentdate.strftime("please attend the event on %A, %b ,%d  in year %Y"))
# #%d for date    %b for month %Y is for year
# # %A is for day e.g monday ,sunday etc.

#calculate your days until your birthdate

birthday=input("please enter your birthdate in formate of (mm/dd/yyyy) :") # the input function always return string

birthdate= datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
print(birthdate)
age=(currentdate-birthdate)
print("you are ",age.days,"days old")
agemonth=age/30

print("you are ",agemonth.days,"month old")
ageYear=agemonth/12
print("you are",ageYear.days,"years old")
#date time is twice because datetime is module in datetime class and strptime is function in datime module
#print=("your bith month is "+ birthdate).strptime("%B")
