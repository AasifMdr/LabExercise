'''
Write a function called show_stars(rows).If rows is 5, it should print the following:*
'''

def showstars(rows):
    for i in range(1, rows):
        print('*' * i)
ant = int(input("Enter the number of rows: "))
(showstars(ant))