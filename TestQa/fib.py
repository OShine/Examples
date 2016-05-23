#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys


def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


print(fib(2000))
