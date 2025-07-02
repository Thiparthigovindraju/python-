import datetime
currentDate=datetime.datetime.now()
birthDate=datetime.datetime(2003,8,27)
z=currentDate.year-birthDate.year
y=birthDate.strftime("%A")
print(z)
print(y)
