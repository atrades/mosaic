import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
if len(sys.argv)<3: 
   print "Enter input list and output folder"; exit(1)
from PIL import Image
i = 1
for line in open(sys.argv[1]):
  img = Image.open(line.strip())
  print line.strip()
  img = img.convert('L')
  img.save(sys.argv[2]+("/%05d.jpg"%(i)))
  i+=1
