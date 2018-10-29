#!/usr/bin/env python
import sys
STEPX = 4
STEPY = 4
if len(sys.argv)<2: 
   print "Enter input image"; exit(1)
from PIL import Image
im = Image.open(sys.argv[1])
w = im.width
h = im.height
n = 0;m = 0;mat = {}
for i in xrange(0,w,STEPX):
  m=0
  for j in xrange(0,h,STEPY):
    av = 0; cnt = 0 
    for q in xrange(i,min(i+STEPX,w)):
      for z in xrange(j,min(j+STEPY,h)):
         av+=im.getpixel((q,z));cnt+=1
    mat[(n,m)] = av/cnt
    m+=1
  n+=1;

for i in xrange(n):
  for j in xrange(m):
    print mat[(i,j)],
  print
