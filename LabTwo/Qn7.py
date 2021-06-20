'''
Given a positive real number, print its fractional part.
'''

num = float(input("Enter a positive real number: "))
i = int(num)
f = num - int(num)
print(f'Its fractional part is {f}')
