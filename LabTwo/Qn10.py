'''
Write a Python program to sum of three given integers.
However, if two values are equal sum will be zero.
'''

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
sum = 0
if a != b and b != c and c != a:
    sum = a + b + c
print(f"The sum is {sum}")