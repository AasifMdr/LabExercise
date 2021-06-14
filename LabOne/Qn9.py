'''
Write a python program to find sum of the first n positive integers.
sum = (n*(n+1)) / 2
'''

num = int(input("Enter a positive integer: "))
sum = (num * (num + 1)) / 2
print(f'The sum of the first {num} positive integers is {sum}')