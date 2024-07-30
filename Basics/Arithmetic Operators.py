#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      snmor
#
# Created:     30-07-2024
# Copyright:   (c) snmor 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

One = int(input("Enter 1st Number "))
Two = int(input("Enter 2nd Number "))

print(One)
print(Two)

#Arithmetic Operators
print(One + Two)
print(One - Two)
print(One * Two)
print(One / Two)
print(One % Two)
print(One // Two)
print(One ** Two)

#Shortcuts
One = One+10
One += 10
Two -= 5
One *= 2

print(One)
print(Two)

#Operator precedence
New = 2+(3*4)/2**2
print(New)