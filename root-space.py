#!/usr/bin/python
import os, sys, string

used_root=os.popen("df -h / | grep -v Filesystem | awk '{print $5}'| sed s/\%//").readline().strip()

du=int(used_root)

if used_root < "85%":
        print "OK - %s percent of root disk space used." % used_root
        sys.exit(0)
elif used_root == "85%":
        print "WARNING - %s percent of root disk space used." % used_root
        sys.exit(1)
elif used_root > "85%":
        print "CRITICAL - %s percent of root disk space used." % used_root
        sys.exit(2)
else:
        print "UKNOWN - %s percent of root disk space used." % used_root
        sys.exit(3)
