#  center_crop
# 이미지 왜곡 없이 정사각형을 만드려면 잘라야한다.
# 가로 세로 중 짧은 쪽을 기준으로 가운데를 자른다.

from PIL import Image

def center_crop(im):
    crop_size = min(im.size)

    left = (im.size[0] - crop_size)//2  # 몫을 구한다.
    top = (im.size[1] - crop_size)//2
    right = (im.size[0] + crop_size) // 2
    bottom = (im.size[1] + crop_size) // 2

    return im.crop((left, top, right, bottom))  # 튜플을 매개변수로

im = Image.open('python.png')
cropImage = center_crop(im)
cropImage.save('python-crop(2).jpg')
cropImage.show()

# 정보 손실이 발생할 수 있다.
# 가로 세로 중 긴쪽을 기준으로 정사각형을 만들면 정보 손실이 없다. (채우는 부분은 디폴트 값)
# How -> 정사각형을 만들고 가운데에 이미지를 덮어써준다.
