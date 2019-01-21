#!/usr/bin/env python

import os
import sys
import re

try:

   jobid = os.environ['PBS_JOBID']  
   fin = open(sys.argv[1],'r')
   fout = open(sys.argv[2],'w')
   for line in fin:
      if not re.match(r'^\s*$',line):
        fout.write(line)

   fin.close()
   fout.close()
     
except:
  print "I will only run if submitted via the queue system. "

