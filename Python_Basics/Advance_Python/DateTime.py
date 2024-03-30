from datetime import date
from datetime import datetime
date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2
print(result)
print(type(result))

print(result.days)


datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

result2 = datetime1 - datetime2
print(result2)

print(result2.seconds)
print(result2.total_seconds())