'''
Given a positive real number, print its fractional part.
'''

num = float(input("Enter a positive real number: "))
fractional_part = num - int(num)
print(f'Its fractional part is {fractional_part}')
