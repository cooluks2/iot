#  썸네일 만들기 - .thumbnail

from PIL import Image

im = Image.open('python.png')

# Thumbnail 이미지 생성
size = (64, 64)
im.thumbnail(size)  # 변수 im의 원본을 변경시킴
                    # 가로 세로 비율을 유지하면서 줄여줌(긴쪽에 맞춘다)

im.save('python-thumb.jpg')
im.show()

print(im.size)

"""
// 64x43 이미지 저장됨
"""
