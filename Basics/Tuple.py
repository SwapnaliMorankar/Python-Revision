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

#Tuples are immutble so we cannot add or insert any item externally once declared
Students = ("Swapnali", "Raj", "Aabha", "Harsh", "Dhanashree", "Raj", "Raj")


#Tuples only have 2 methods

#Count
print(Students.count("Raj"))
print(Students.count("Aabha"))

#index
print(Students.index("Swapnali"))
print(Students.index("Harsh"))