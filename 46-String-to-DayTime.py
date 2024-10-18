#string to daytime
from datetime import datetime
from dateutil  import parser
date ="oct 14 2024 9:32PM"
# print(type(date))
date_time=datetime.strptime(date, "%b %d %Y %I:%M%p")
print(date_time)
# print(type(date_time))
#or
date_time2=parser.parse(date)
print(date_time2)