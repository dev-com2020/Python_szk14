# from datetime import date
# import calendar as c
from datetime import datetime
from zoneinfo import ZoneInfo

#
# dzis = date.today()
# print(dzis)
# print(dzis.ctime())
# print(dzis.day, dzis.month, dzis.year)
# # print(c.calendar(2022))
# print(dzis.weekday())
# print(c.day_name[dzis.weekday()])
# print(dzis.isoformat())
now = datetime.now()
print(now)
print(now.date())
print(now.time())
czas = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(czas)




