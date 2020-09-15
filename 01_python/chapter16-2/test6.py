#  이미지 회전 및 Resize - .resize, .rotate

from PIL import Image
im = Image.open('python.png')

# 크기를 600x600 으로
img2 = im.resize((600, 600))
img2.save('python-600.jpg')
img2.show()

# 90도 회전 (기존 사이즈에서 이미지만 반시계 방향으로 90도 회전)
img3 = im.rotate(90)
img3.save('python-rotate.jpg')
img3.show()

