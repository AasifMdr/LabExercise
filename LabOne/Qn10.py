'''
Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

sec = int(input("Enter the number of seconds: "))
day = sec // 86400
rem_sec = sec % 86400
hours = rem_sec // 3600
rem_hours = rem_sec % 3600
minutes = rem_sec // 60
seconds = rem_hours % 60
print(f'The converted data is {day} days, {hours} hours, {minutes} minutes, and {sec} seconds.')
