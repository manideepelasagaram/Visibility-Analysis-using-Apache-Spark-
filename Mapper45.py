#!/usr/bin/env python
import sys
for line in sys.stdin:
    data = line.strip()
    (month, skyHeight, qlty) = (data[19:21], data[70:75], data[75:76])
    if(skyHeight != '99999' and qlty in ['0','1','4','5','9']):
        print "%s\t%s" % (month, skyHeight)

