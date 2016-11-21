#!/usr/bin/env python

a = [3, 9, 8, 5, 2]
b = [1, 4, 9, 2, 6]
print sum(x*y for x,y in zip(a, b))

