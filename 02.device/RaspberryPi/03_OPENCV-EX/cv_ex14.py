import cv2
# import numpy as np

img = cv2.imread('./data/lena.jpg')

# for y in range(100, 400):
#   x in range(200, 300):
#       img[y, x, 0] = 255 # B-채널을 255로 변경

img[100:400, 200:300, 0] = 255 # B-채컬을 255로 변경
img[100:400, 200:300, 1] = 255 # G-채컬을 255로 변경
img[100:400, 200:300, 2] = 255 # R-채컬을 255로 변경

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()