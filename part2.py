"""
******
PART 2
******
Write a program that asks the user to enter a positive integer n. The program will then print the sum of the first n positive cubes.

For example, if the user types in 4, the program should print 100 (since 1^3 + 2^3 + 3^3 + 4^3 = 100).
"""

#write your code here
n = int(input("Enter a positive number: "))
 
for x in range(1, n + 1):
 print(x**3)


b = int(input("Enter the base: "))
h = int(input("Enter the height: "))
 
for x in range(h):
 print("*" * b)

