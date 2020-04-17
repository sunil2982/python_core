# datetime module also used for time mainpulation
import datetime
currentTime=datetime.datetime.now() # now is a method
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
print(datetime.datetime.strftime(currentTime,"%I:%M:%S:%p"))

# %H is for 24 hour clock ,%M for minute %Sfor second(%s is for string input)
#  %p for am or pm %I for 12hour clock