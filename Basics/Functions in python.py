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

#python has 3 types of functions
#In-built functions
#Example - int(), str(), len()

#Module functions
#Can be accessed only by importing particular modules

import math
print(dir(math))

from math import *
print(sqrt(25))
print(cos(90))


#User defined Functions
#Syntax

#    def function_name(parameters):
#        //Body of fucntion