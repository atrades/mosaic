import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
if len(sys.argv)<2: 
   print "Enter image path"; exit(1)
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

#img=mpimg.imread(sys.argv[1])
#gray = rgb2gray(img)    
#plt.imshow(gray, cmap = plt.get_cmap('gray'))
#plt.show()
from PIL import Image
img = Image.open(sys.argv[1])
img.thumbnail((800, 600), Image.ANTIALIAS) # resizes image in-place
imgplot = plt.imshow(img)
plt.show()
