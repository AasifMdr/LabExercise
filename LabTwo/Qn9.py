'''
Check whether the given year is leap year or not.
If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
• a year is always a leap year if its number is exactly divisible by 400
'''

yr = int(input("Enter a year: "))
if yr / 4 == yr // 4:
    print(f"It is a leap year.")
else:
    print(f"It is a common year.")