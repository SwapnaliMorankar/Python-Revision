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

Age = int(input("Enter your Age"))

if(Age>=18 and Age<60):
    print("You are eligible")
elif(Age>=60 and Age<=100):
    print("You are not eligible")
else:
    print("Wrong")