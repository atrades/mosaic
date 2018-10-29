#!/usr/bin/env python
import sys
SCALEW=200
SCALEH=200
MATW=150
MATH=150
if len(sys.argv)<4: 
   print "Enter input matrix file, file list with values and output file"; exit(1)
from PIL import Image
import random
imgs = []
for line in open(sys.argv[2]):
   line = line.strip().split()
   imgs.append((int(line[0]),line[1]))

#print imgs

def getFile(imgs,v):
   i=0;
   while i<len(imgs) and v>imgs[i][0]: 
     i+=1
   vals = [i]
   if i<2: vals = range(2)
   elif i>len(imgs)-2: vals = range(len(imgs)-2,len(imgs))
   else: vals = range(i-2,i+2)
   q = random.choice(vals)
   return imgs[q][1]

im = Image.new('L',(MATW*SCALEW,MATH*SCALEH))
x = 0
for line in open(sys.argv[1]):
    vals = map(int,line.strip().split())
    y = 0
    for v in vals:
       picfile = getFile(imgs,v)
       pic = Image.open(picfile)
       dd = min(pic.width,pic.height)
       pic = pic.crop((0,0,dd,dd))
       pic.thumbnail((SCALEW,SCALEH),Image.ANTIALIAS)
       im.paste(pic,(SCALEW*x,SCALEH*y))
       y+=1
    x+=1
    print x,"line generated"
im.save(sys.argv[3])
im.show()
