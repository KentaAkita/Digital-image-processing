# 2017/7/?
import cv2
import numpy as np
import size
from numba import jit
import time

start = time.time()

img = cv2.imread("hoge", 0)
img = 255 - img

cv2.imshow("negaposi", img)
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time))
cv2.waitKey()
cv2.destroyAllWindows()
