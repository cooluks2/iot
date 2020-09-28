import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')

rows, cols, channels = src.shape
M1 = getRoationMatrix2D((rows/2, cols/2), 45, 0.5) # 중심좌표, 회전각, 배율
M2 = getRoationMatrix2D((rows/2, cols/2), -45, 1.0)
dist1 = cv2.wrapAffine(src, M1, (rows,cols))
dist2 = cv2.wrapAffine(src, M2, (rows,cols))

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey(0)
cv2.destroyWindows()