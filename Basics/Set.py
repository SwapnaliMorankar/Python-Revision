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

#Set
#Set doesnt allow duplicate values in it

Marks = {23, 45, 77, 56, 89, 63, 45}
print(Marks)

#Set values cannot be get using indexes, therefore called unordered
#We compulsory need loop for it

for i in Marks:
    print(i)


#Dictionary
#Dictionary structure stores key values pairs

Data = {"English": 98 , "Hindi" : 75, "Chemistry": 39, "Physics": 87}
print(Data)

#print a value
print(Data["Hindi"])

#Add a pair
Data["Biology"] = 90
print(Data)

#Change exisiting marks
Data["Hindi"] = 60
print(Data)


