#!/usr/bin/env python
import sys

hrange = [0] * 13
max_val = [0] * 13
min_val = [99999] * 13

for line in sys.stdin:
    key, val = line.strip().split("\t")
    month = int(key)
    skyHeight = int(val)

    if skyHeight > max_val[month]: 
        max_val[month] = skyHeight

    if skyHeight < min_val[month]:
        min_val[month] = skyHeight

    hrange[month] = max_val[month] - min_val[month]

for month in range(1, 13):
    print("%s\t%s" % (month, hrange[month]))
