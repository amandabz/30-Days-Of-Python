# Dates

# Datetime
# import de un módulo que ya viene dentro de Python
from datetime import datetime

now = datetime.now()  # función dentro de datetime

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

timestamp = now.timestamp()  # timestamp es una representación única de un tiempo

print(timestamp)


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


year_2024 = datetime(2024, 1, 1)  # Mínimo que necesitamos para definir un año
print(year_2024)

print_date(year_2024)


# Time

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# Date

from datetime import date

current_date = date.today()  # Fecha de hoy

print(current_date)


current_date = date(2023, 7, 30)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)


diff = year_2024 - now  # Quedan 331 días para llegar a la fecha de year_2024
print(diff)

diff = year_2024.date() - current_date  # Quedan 124 días para llegar a la fecha de current_date
print(diff)


# Timedelta
# Nos sirve para trabajar y operar con diferencias de fechas
# Nos vale para decir: "esto es un  espacio de tiempo que dura X"

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)  # Definimos weeks porque nos hemos salido del orden
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)


