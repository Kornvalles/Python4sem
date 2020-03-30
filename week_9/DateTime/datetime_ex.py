from datetime import date, timedelta, datetime, time

today = date.today()
today = date(today.year, today.month, today.day)
print(type(today))
print(today)


next_lecture = today + timedelta(days=7)
time_to_next_lecture = abs(next_lecture - today)
print(time_to_next_lecture.days)

next_lecture = date(2020, 2, 24) + timedelta(weeks=2)
time_to_next_lecture = abs(next_lecture - today)
print(time_to_next_lecture.days)

print(today.strftime("%d/%m/%y"))
print(today.strftime("%A %d. %B %Y"))

t = time(12, 10, 30)
print(t.isoformat())

