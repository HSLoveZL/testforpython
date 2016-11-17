#!/usr/bin/env python
# _*_ coding=utf-8 _*_
# 100 inside can be divided by 3
L = []
for x in range(1, 101):
    if x % 3 == 0:
	L.append(x)

print L

