#!/bin/python3

from scripts import weirdo_function

def test_weirdo_function_is_weird():
   assert weirdo_function(5) == 'Weird'
   
   
def test_weirdo_function_is_not_weird():
   assert weirdo_function(56) == 'Not Weird'
   
      
def test_weirdo_function_with_negative_number():
   assert weirdo_function(-1) == 'Weird'
   
def test_weirdo_function_with_char():
   assert weirdo_function('a') == 'Must pass in a Integer value'

def test_weirdo_function_with_string():
   assert weirdo_function('abcd') == 'Must pass in a Integer value'
