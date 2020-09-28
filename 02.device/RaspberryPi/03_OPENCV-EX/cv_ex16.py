import cv2
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

# dst = src # 참조
dst = src.copy()# 복사
dst[100:400, 200:300] = 0

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()