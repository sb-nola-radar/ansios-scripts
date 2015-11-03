#!/usr/bin/python
import os, sys, string

used_web=os.popen("df -h /var/www| grep -v Filesystem | awk '{print $5}'| sed s/\%//").readline().strip()

du=int(used_web)

if du < "85%":
        print "OK - %s percent of web disk space used." % used_web
        sys.exit(0)
elif du  == "85%":
        print "WARNING - %s percent of web disk space used." % used_web
        sys.exit(1)
elif du > "85%":
        print "CRITICAL - %s percent of web disk space used." % used_web
        sys.exit(2)
else:
        print "UKNOWN - %s percent of web disk space used." % used_web
        sys.exit(3)
