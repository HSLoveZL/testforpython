#!/usr/bin/evn python
# _*_ coding=utf-8 _*_
raw = "Do you love Java? Java is a good programme language."
raw_l = raw.split(" ")
for i, string in enumerate(raw_l):
    if "Java" in string:
	raw_l[i] = "PHP"
print raw_l

raw_l01 = raw_l[:15]
raw_l02 = raw_l[16:]
print (" ".join(raw_l))

