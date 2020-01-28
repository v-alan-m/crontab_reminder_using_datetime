'''
Take the data from the file called crontab in the same folder as this script,
and using the command line entry: python next_update.py 16:10 < crontab
Given the user's input time, the next time the cron jobs will be fired will 
be printed within terminal
'''

# Import required modules and classes
import sys
import datetime as dt
from croniter import croniter

# Intialise variables for global use
time_format = "%H:%M"
# Define starting date.day()
curr_year = dt.datetime.now().year
curr_month = dt.datetime.now().month
curr_day = dt.datetime.now().day
# Length of the command line arguements
len_argv = len(sys.argv)
# Will not intialise time_string until given a stdin string input
if len(sys.argv) > 1: time_string = sys.argv[1]

# Check if the number of command line arguments provided is correct, provides hints regarding format
def argv_num_check(len_argv):
    if len_argv > 2:
        print("Only a single time arguement is required in the HH:MM format, E.g. 16:10")
    elif len_argv < 2:
        print("A time arguement is required in the following format: HH:MM, E.g. 16:10")
    else:
        print("Please exit the program and type in < followed by the input file name: E.g < crontab")
        return True

# Check the if the time arguement is the correct format, and converts it into a dt.datetime object for use later
def datetime_format(time_string):
    try:
        return dt.datetime.strptime(time_string, time_format)
    except:
        raise ValueError("Incorrect time format. Change to: HH:MM (E.g. 16:10)")

# Print the times and day when the cron jobs will be fired next, along with the file location
def next_update():
# Read the data that has been entered into stdin, and each new line will be read as a seperate list
    crontab_list = sys.stdin.readlines()

# Iterate through each line (list object) of the crontab file
    for i in range(len(crontab_list)):
# Split the the list object for each read line, using the whitespaces 
        crontab_time = crontab_list[i].split()

# Minutes and hours respectively from crontab: Check if the first element is an '*' or not, if not convet it into an integer
        stdin_minuntes = crontab_time[0]
        stdin_hours = crontab_time[1]

# Define the command line input time
        curr_hour = datetime_format(sys.argv[1]).hour
        curr_minutes = datetime_format(sys.argv[1]).minute

# format: dt.datetime(year, month, day, hour, minute), the command line arguement time is inserted hereinput_minute
        command_line_time = dt.datetime(curr_year,curr_month,curr_day,curr_hour,curr_minutes)
# format: croniter(min, hour, day, month, day_of_week), use croniter().get_next() to iterate through the time information in crontab
        next_time_datetime = croniter(f'{stdin_minuntes} {stdin_hours} * * *',command_line_time).get_next(dt.datetime)
# Find next timem the cron files will fire and ensure the time format is correct
        next_time = next_time_datetime.time().strftime(time_format)

# Check if the next update is today or tomorrow:
        if next_time_datetime.date() > command_line_time.date():
            next_day = "Tomorrow"
        else:
            next_day = "Today"

# Print the next cron time details
        print(f"{next_time} {next_day} {crontab_time[2]}")

# Have the time string format checked, and if the format is correct then print cron times
def main():
    if argv_num_check(len_argv):    
        if datetime_format(time_string):
            next_update()

if __name__ == "__main__":
    main()
