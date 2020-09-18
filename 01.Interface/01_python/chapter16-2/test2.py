#  색상 변경 -> .convert

from PIL import Image

# convert : "L" (gray), "RGB", "RGBA", "CMYK"
im = Image.open('python.png').convert("L")  # 메서드 체이닝

im.save('python-gray.jpg')
im.show()

"""
//흑백사진 뜸
"""

