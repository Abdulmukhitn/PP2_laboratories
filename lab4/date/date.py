from datetime import datetime
from datetime import timedelta

#1
now= datetime.now()
day5ago= now - timedelta(days=5)

print(day5ago)

#2

yesterday= now - timedelta(days= 1)
tomorrow= now + timedelta(days=1)
print(yesterday)
print(now)
print(tomorrow)

#3

without_micro= now.replace(microsecond=0)

print(without_micro)

#4 
date_1= datetime(2011, 10,10,12,0,0)
date_2= datetime(2011, 10,10,11,0,0)
diff= (date_1 - date_2)

print(diff)