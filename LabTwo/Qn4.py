'''
Given three integers, print the smallest one.
(Three integers should be user input)
'''

a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))
c = int(input('Enter the third integer: '))
if a < b and a < c:
    print(f"{a} is the smallest number.")
elif b < a and b < c:
    print(f"{b} is the smallest number.")
elif c < a and c < b:
    print(f"{c} is the smallest number.")
