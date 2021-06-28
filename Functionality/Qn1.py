'''
Write a Python function to find the Max of three numbers.
'''

def max():
    a=int(input('Enter number: '))
    b=int(input('Enter number: '))
    c=int(input('Enter number: '))
    if a>b and a>c :
        print(f'{a} is the max number.')
    elif b>a and b>c:
        print(f'{b} is the max number.')
    elif c>b and c>a:
        print(f'{c} is the max number.')
max()