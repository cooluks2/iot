import cv2
import matplotlib.pyplot as plt

imageFile = './data/lena.jpg'
img_bgr = cv2.imread(imageFile)

plt.axis('off')
plt.imshow(img_bgr)
plt.show()

plt.axis('off')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()