'''
Take the data from the file called crontab in the same folder as this script,
and using the command line entry: python next_update.py 16:10 < crontab
Given the user's input time, the next time the cron jobs will be fired will
be printed within terminal
'''

from sys import argv, stdin
import datetime as dt
from croniter import croniter

time_format = "%H:%M"

# Define starting date.day()
curr_year = dt.datetime.now().year
curr_month = dt.datetime.now().month
curr_day = dt.datetime.now().day

def datetime_format(time_string):
    """Check the if the time arguement is the correct format, and converts it into a dt.datetime object for use later."""
    try:
        return dt.datetime.strptime(time_string, time_format)
    except:
        raise ValueError("Incorrect time format. Change to: HH:MM (E.g. 16:10)")

def print_next_updates(time_str):
    """Print the times and day when the cron jobs will be fired next, along with the file location."""
    crontab_list = stdin.readlines()

    for i in range(len(crontab_list)):
        crontab_time = crontab_list[i].split()

        stdin_minuntes = crontab_time[0]
        stdin_hours = crontab_time[1]

        curr_hour = datetime_format(time_str).hour
        curr_minutes = datetime_format(time_str).minute

        command_line_time = dt.datetime(curr_year,curr_month,curr_day,curr_hour,curr_minutes)
        next_time_datetime = croniter(f'{stdin_minuntes} {stdin_hours} * * *',command_line_time).get_next(dt.datetime)
        next_time = next_time_datetime.time().strftime(time_format)

        if next_time_datetime.date() > command_line_time.date():
            next_day = "Tomorrow"
        else:
            next_day = "Today"

        print(f"{next_time} {next_day} {crontab_time[2]}")

# Have the time string format checked, and if the format is correct then print cron times
def main():
    len_argv = len(argv)

    if len_argv != 2:
        print("Expected a single argument in HH:MM format, eg 16:10.")
        exit(1)

    if datetime_format(argv[1]):
        print_next_updates(argv[1])

if __name__ == "__main__":
    main()
