'''
A school decided to replace the desk in their classroom.
Each desk sits two students.
Given the number of sts in each class, print the smallest possible number
of desk that can be purchased.
The program should read 3 int: the numb of sts in each of the 3 classes
a, b and c resp.
'''

import math
Students_classA = int(input("Number of Students in class A: "))
Students_classB = int(input("Number of Students in class B: "))
Students_classC = int(input("Number of Students in class C: "))
a = math.ceil((Students_classA/2))
b = math.ceil((Students_classB/2))
c = math.ceil((Students_classC/2))
print(f"The number of desk required in total {a+b+c}")