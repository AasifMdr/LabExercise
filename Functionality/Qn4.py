'''
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit(parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20
'''

def mul35(limit):
    sum = 0
    for i in range(1, limit):
        if i/3 == i//3 or i/5 == i//5:
            sum = sum + i
    return sum
a = int(input("Enter a limit: "))
print(mul35(a))
