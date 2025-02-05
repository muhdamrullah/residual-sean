from PIL import Image
import numpy as np
import sys
import os
from scipy import ndimage
import cPickle as pickle
import gzip
import scipy
import random

if len(sys.argv) < 2:
    print "Usage: python process_single.py input_folder/"
    exit(1)

# input folder
fi = sys.argv[1]

# init var
classes = os.listdir(fi)
set_x = []
set_y = []
k = 0 # idx for classes
list_classes = []
new_im = []
counter = 0
index_files = 6

# Create sets
for cls in classes:
        list_classes.append(cls)
        imgs = os.listdir(fi + cls)
        for img in imgs[index_files*2500 : (index_files + 1) * 2500]:
                im = ndimage.imread(fi + cls + '/' + img)
                # To resize any image to 32 x 32
                im = scipy.misc.imresize(im,(32,32)) 
                r = im[:,:,0].flatten()
                g = im[:,:,1].flatten()
                b = im[:,:,2].flatten()
                new_im.append(list(r) + list(g) + list(b))
                print k
		counter += 1
		print counter
                set_x.append(new_im)
                set_y.append(k)
        k +=1
########################################
#Randomize both list
#print "Begin Rendomizing"
#set_both = list(zip(set_x, set_y))
#random.shuffle(set_both)
#set_x, set_y = zip(*set_both)

#########################################

set_x = np.array(new_im, np.uint8)
print set_x.shape
print set_x
image_dictionary = {}
image_dictionary['data'] = set_x
image_dictionary['label'] = set_y

with open('data_batch_%s' % (index_files+1), 'wb') as f:
    pickle.dump(image_dictionary, f, -1)
f.close()
