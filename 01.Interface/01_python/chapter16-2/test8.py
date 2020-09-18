#  이미지 <--> numpy 배열 - .array, .fromarray
# numpy도 외부 라이브러리이다.

from PIL import Image
import numpy as np

im = Image.open('python.png')

# Image --> numpy array (3차원 데이터)
im2arr = np.array(im)  # im2arr.shape: height x width x channel
print(im2arr.shape)

# numpy array --> Image
arr2im = Image.fromarray(im2arr)

# 그냥 실행하면 ModuleNotFoundError: No module named 'numpy' 가 나온다.
# >> pip install numpy
# 픽셀 단위의 작업을 할 때 사용

"""
(333, 500, 3)
"""
