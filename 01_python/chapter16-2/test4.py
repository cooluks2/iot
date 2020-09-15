#  이미지 부분 잘라내기 - .crop
from PIL import Image

im = Image.open('python.png')
cropImage = im.crop((100, 100, 150, 150)) # (좌, 상, 우, 하)
# 사진의 최 좌측상단이 원점이다.
# (x1, y1, x2, y2) -> 좌상단(x1, y1) 우하단(x2,y2)
cropImage.save('python-crop.jpg')
cropImage.show()

"""
// 부분만 저장됨
"""

