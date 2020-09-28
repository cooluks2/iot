import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.resize(src, dsize=(320, 240))
dst2 = cv2.resize(src, dsize=(0,0), fx=1.5, fy=1.2)

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyWindows()