'''
Write a program that reads the length of the base and the height of a right-angled triangle and prints the area.
Every number is given on a separate line.
'''

base = int(input("Enter the base of a triangle: "))
height = int(input("Enter the height of a triangle: "))
area = (base * height) / 2
print(f"The area of the given triangle is {area}")