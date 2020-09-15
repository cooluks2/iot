#  이미지 필터링 - .filter

from PIL import Image, ImageFilter

im = Image.open('python.png')
blurImage = im.filter(ImageFilter.BLUR)  # 다른 필터는 검색해보자.

blurImage.save('python-blur.png')

# 선명한 이미지는 컴퓨터가 처리하기에 안좋다. -> .filter(ImageFilter.BLUR)

