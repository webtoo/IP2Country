#!/usr/bin/python

import os
import pygeoip 

## Open the file with read only permit
f = open('/root/ip.csv', "r")

gi = pygeoip.GeoIP('/root/GeoIP.dat')
for line in f:
    line = line.replace('\n', '')    # remove '\n' only
    country = gi.country_name_by_addr(line)
    print line,',',country
f.close()
