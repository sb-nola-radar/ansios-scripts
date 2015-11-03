#!/usr/bin/python
import os, sys, string

used_log=os.popen("df -h /var/log | grep -v Filesystem | awk '{print $5}'| sed s/\%//").readline().strip()

du=int(used_log)

if du < "85":
        print "OK - %s percent of log disk space used." % used_log
        sys.exit(0)
elif du == "85":
        print "WARNING - %s percent of log disk space used." % used_log
        sys.exit(1)
elif du > "85":
        print "CRITICAL - %s percent of log disk space used." % used_log
        sys.exit(2)
else:
        print "UKNOWN - %s percent of log disk space used." % used_log
        sys.exit(3)
