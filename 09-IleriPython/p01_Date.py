from datetime import datetime

result = dir(datetime)
#print(result)

simdi = datetime.now()
simdi = datetime.today()

print(simdi.year)
print(simdi.month)
print(simdi.day)
print(simdi.hour)
print(simdi.minute)
print(simdi.second)

print(datetime.ctime(simdi))
print(datetime.strftime(simdi,"%y"))
print(datetime.strftime(simdi,"%x"))
print(datetime.strftime(simdi,"%d"))
print(datetime.strftime(simdi,"%m"))
print(datetime.strftime(simdi,"%A"))
print(datetime.strftime(simdi,"%B"))
print(datetime.strftime(simdi,"%Y %B %M  %A"))

t = "15 April 2019 hour 10:12:30"
dt = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(dt)
dt.year


birthday = datetime(1994,1,1,17,47,25)
print(birthday )

print(datetime.timestamp(birthday))
