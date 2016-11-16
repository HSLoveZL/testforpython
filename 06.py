#!/usr/bin/env python
# _*_ coding=utf-8 _*_
import random
number = random.randint(1, 101)
guess = 0

while True:
    num_input = raw_input("please input one interger that is in 1 to 100:")
    guess += 1
    if not num_input.isdigit():
	print "please input a interger."
    elif int(num_input) < 0 or int(num_input) >= 100:
	print "The number should be in 1 to 100"
    else:
	if number == int(num_input):
	    print "OK, you are good. It is only %d, then you succeed." % guess
	    break
	elif number > int(num_input):
	    print "your number is more less."
	elif number < int(num_input):
	    print "your number is bigger."
	else:
	    print "There is something bad, I will not work"

