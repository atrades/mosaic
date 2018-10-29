#!/usr/bin/env python
import sys
SCALEW=200
SCALEH=200
if len(sys.argv)<3: 
   print "Enter input list file and output file"; exit(1)
from PIL import Image
imgs = []
for line in open(sys.argv[1]):
   line = line.strip()
   print line
   im = Image.open(line)
   dd = min(im.width,im.height)
   pic = im.crop((0,0,dd,dd))
   pic.thumbnail((SCALEW,SCALEH),Image.ANTIALIAS)
   ave = 0
   for i in xrange(SCALEW):
     for j in xrange(SCALEH):
       ave+=pic.getpixel((i,j))
   imgs.append((ave/(SCALEW*SCALEH),line))
out = open(sys.argv[2],'w')
imgs = sorted(imgs)
for val in imgs:
  out.write("%s %s\n" % val)
out.close()
