#!/usr/bin/python
# -*- coding: latin-1 -*-
# python 3.5
import os
import sys

while True:
    try:
        x = int(input("Enter the number for check: "))
    except ValueError:
        print('The entered value should be an integer. Please, try again.')
    else:
        if x < 0:
            x = 0
            print('The negative one, value has changed to zero.')
        elif x == 0:
            print('Zero.')
        elif x == 1:
            print('The One.')
        else:
            print('The entered value is more than One.')
