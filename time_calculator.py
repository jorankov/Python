""" El siguiente programa simula cómo se modifica un horario de inicio con respecto a una duración determinada,
de acuerdo al día que se le dé como input 

start = horario de inicio
duration = tiempo que se le agregará a start
day = día en el que inicia el horario

el output deberá mostrar el horario modificado 
(AM o PM, depende de la modificación del resultado final).
Si el horario superó las 12PM, el día también será modificado.
"""


def add_time(start: str, duration: str, day: str = ""):
    duration = duration.split(":")

    time_split = start.split(":")  # Separa los elementos por :
    hours = time_split[0]  # Devuelve la hora
    mins_split = time_split[1].split()  # Separa minutos del AM/PM
    mins = mins_split[0]  # Devuelve los minutos

    am_pm = mins_split[1]  # Devuelve AM/PM

    hours_duration = duration[0]  # Hora de la duracion
    mins_duration = duration[1]  # Minutos de la duracion

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    count = 0
    if day in days:
        posicion = days.index(day)
        count += posicion

    days_count = 0

    suma_h = int(hours) + int(hours_duration)
    suma_m = int(mins) + int(mins_duration)
    while suma_m >= 60:
        suma_m -= 60
        suma_h += 1
    while suma_h >= 12:
        suma_h -= 12
        count += 1
        days_count += 1

    while count > 7:
        count -= 7
    count = count

    am_pm = "AM" if days_count % 2 == 0 else "PM"

    if days_count == 0:
        days_later = ""
    elif days_count == 1:
        days_later = "(next day)"
    else:
        days_later = f"({days_count} days later)"

    if suma_h < 10:
        suma_h = "0" + str(suma_h)
    if suma_m < 10:
        suma_m = "0" + str(suma_m)

    new_time = print(f"{suma_h}:{suma_m} {am_pm}, {days[count]} {days_later}")

    return new_time


# Test cases
print("\n")
add_time("06:06 AM", "01:40")
add_time("12:06 AM", "02:40", "Tuesday")
add_time("11:06 PM", "24:02", "Wednesday")
add_time("01:50 AM", "950:40", "Friday")
print("\n")
