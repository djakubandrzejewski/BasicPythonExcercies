from datetime import date, datetime

date_components = input().split('.')

day, month, year = [int(item) for item in date_components]

d = date(year, month, day)
y = d.timetuple().tm_yday

print(y)
