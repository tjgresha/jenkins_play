#!/bin/python3

import math
import os
import random
import re
import sys



def weirdo_function(n):
   if (isinstance(n ,int)):
      am_i_odd = " "   
      if n % 2 ==1 or n in range(5,21):
         am_i_odd  = 'Weird'
      else:
         am_i_odd  = 'Not Weird'
      return am_i_odd 
   else:
      return("Must pass in a Integer value")


