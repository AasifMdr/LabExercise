'''
Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number
'''

def fizz_buzz(b):
    if b/3 == b//3 and b/5 == b//5:
        return "FizzBuzz"
    elif b/5 == b//5:
        return "Buzz"
    elif b/3 == b//3:
        return "Fizz"
a = float(input("Enter a number: "))
print(fizz_buzz(a))