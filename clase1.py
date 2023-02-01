# ejercicios clase 1 introduccion
import cv2 as cv
import numpy as np
s = 100
im = np.zeros([100,100])
print(im)

for i in range(s):
    im[i,i]= 255
print(im)
cv.imwrite('imagen1.jpg', im)

