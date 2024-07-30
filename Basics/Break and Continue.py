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

#Break keyword
Students = ["Swapnali", "Aabha", "Raj","Dhanashree", "Harsh", "Arnav"]

for i in Students:
    if( i == "Harsh" ):
        break;
    print(i)
print("End")

#continue keyword
for i in Students:
    if( i == "Harsh" ):
        continue;
    print(i)
print("End")
