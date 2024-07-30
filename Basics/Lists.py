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

#Index 0, 1, 2
Marks = [99, 45, 67, 89, 66, 56]
print(Marks)
print(Marks[1])
print(Marks[5])
print(Marks[1:4])
print(Marks[:4])


#Index -1, -2, -3
Subject = ["English", 101, "Hindi", 368, "Marathi", 900]
print(Subject)
print(Subject[-1])
print(Subject[-3])
print(Subject[-5:-1])


#Using loop in list
for score in Marks:
    print(score)