'''
Given a three-digit number.
Find the sum of its digits.
'''

a = (input("Enter a three-digit number: "))
b = int(a[0]) + int(a[1]) + int(a[2])
print(f'The sum of digits of {a} is {b}')