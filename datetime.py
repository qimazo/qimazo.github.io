from datetime import datetime
import pytz


# user types the time
time_input = input("Please type the time and date of the country you want to convert time from like this: YYYY-MM-DD HH:MM --> ")

# user types source timezone
source_zone = input("From which timezone do you wish to convert time from?(write things like: Europe/Berlin, Asia/Tehran etc)--> ")

# user types destination timezone
target_zone = input("To which timezone do you wish to convert time to?(write things like: Asia/Istanbul, America/New_York etc)--> ")

# turn the typed time into a datetime object
try:
    my_time = datetime.strptime(time_input, "%Y-%m-%d %H:%M")
except:
    print("Unfortunately The time format is wrong. Please use YYYY-MM-DD HH:MM")
    exit()

# try to get the timezones from pytz
try:
    from_tz = pytz.timezone(source_zone)
    to_tz = pytz.timezone(target_zone)
except:
    print("Oops. One of the timezones was typed wrong.")
    exit()

# add the timezone info to the time
from_time = from_tz.localize(my_time)

# convert the time to the new timezone
new_time = from_time.astimezone(to_tz)

# show the result
print()
print("In", source_zone, "it is:", from_time.strftime("%Y-%m-%d %H:%M"))
print("In", target_zone, "it becomes:", new_time.strftime("%Y-%m-%d %H:%M"))