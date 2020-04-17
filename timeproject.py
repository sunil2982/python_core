import datetime
currentdate=datetime.date.today()
#asking userto enter their project end date
projectdate=input("enter your project deadline date in mm/dd/yyyy format :: ")
project_date=datetime.datetime.strptime(projectdate,"%m/%d/%Y").date()
Remaining_days=(project_date-currentdate)
if Remaining_days.days < 0:
    print("opps your deadline is over")
else:
    print("Remaining days for project deadline:: ",Remaining_days.days ,"Days")
    Remaining_weeks=Remaining_days.days/7
    deadlines_days= Remaining_days.days%7
    print("you have %d" %Remaining_weeks,"weeks and %d days" %deadlines_days, "left for your project dead line")
