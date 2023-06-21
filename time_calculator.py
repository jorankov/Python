"""The following program simulates how a start time is modified based on a given duration, according to the day provided as input.

start = start time
duration = time to be added to start
day = day on which the schedule starts

The output should display the modified schedule (AM or PM, depending on the modification of the final result). If the time exceeds 12 PM, the day will also be modified."""


def add_time(start: str, duration: str, day: str = ""):
    duration = duration.split(":")

    time_split = start.split(":")  # Split the elements by :
    hours = time_split[0]  # Returns the hour
    mins_split = time_split[1].split()  # Split minutes from AM/PM
    mins = mins_split[0]  # Returns the minutes

    am_pm = mins_split[1]  # Returns AM/PM

    hours_duration = duration[0]  # Duration hour
    mins_duration = duration[1]  # Duration minutes

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
