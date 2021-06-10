'''
A school decided to replace the desk in their classroom.
Each desk sits two students.
Given the number of sts in each class, print the smallest possible number
of desk that can be purchased.
The program should read 3 int: the numb of sts in each of the 3 classes
a, b and c resp.
'''

classa = int(input("Number of students in class A: "))
classb = int(input("Number of students in class B: "))
classc = int(input("Number of students in class C: "))

a = classa // 2
if classa % 2 == 1:
    a = a + 1

b = classb // 2
if classb % 2 == 1:
    b = b + 1

c = classc // 2
if classc % 2 == 1:
    c = c + 1

print(f'The first group has {classa} number of students so they require {a} desks ')
print(f'The first group has {classb} number of students so they require {b} desks ')
print(f'The first group has {classc} number of students so they require {c} desks ')