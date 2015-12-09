#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
for n in xrange(2, 10):
    for x in xrange(2, n):
        if n % x == 0:
            print n,'=', x, '*', n/x
            break
        else:
            print n, '- простое число'