###Dates###

from datetime import datetime

now = datetime.now()

year_2025 = datetime(2025, 5, 1)
print(year_2025)

def print_date(date):
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.month)
    print(date.year)
    print(date.timestamp())
print_date(now)

from datetime import time

current_time = time(11, 36)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time)

from datetime import date

current_date = date.today()
print(current_date.day)
print(current_date.month)
print(current_date.year)
print(current_date)

current_date = date(2024, 4, 21)
print(current_date.day)
print(current_date.month)
print(current_date.year)
print(current_date)

current_date = date(current_date.year, current_date.month + 1, current_date.day) #asi podriamos modificar las fechas
print(current_date.month)

print(year_2025 - now)
print(year_2025.date() - current_date)


from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

