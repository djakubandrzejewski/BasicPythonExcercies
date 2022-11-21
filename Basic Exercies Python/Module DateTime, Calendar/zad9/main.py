from datetime import date
import calendar
t = date.today()

c = calendar.TextCalendar(calendar.THURSDAY)
str = c.formatmonth(t.year,t.month,w=1)
print(str)
