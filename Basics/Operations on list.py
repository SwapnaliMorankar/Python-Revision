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

Marks = [23, 45, 67, 88, 46, 56, 36]

Marks.append(90)
Marks.insert(1, 33)
print(Marks)
print(56 in Marks)
print(78 in Marks)
print(len(Marks))


#Loop in list
i=0
while(i<len(Marks)):
    print(Marks[i])
    i+=1

Marks.clear()
print(Marks)