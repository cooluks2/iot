# 강의노트 pillow 이미지처리
# 프로젝트 chapter16-2 로 이동

# Pillow 이미지 처리

# PIL

#  PIL
#   ○ 파이썬 이미지 처리 라이브러리
#   ○ pip install pillow
#        아나콘다에 기본 탑재되어 있음
#   ○ 기본 사용방법

# >> pip install pillow  # 터미널
# 이미지파일 프로젝트 폴더에 python.png 다운로드한 상태

####################################################
#  이미지 읽기/저장/화면 출력 - .open, .size, .save, .show

from PIL import Image  # Image는 대문자로 시작하니 Class

# 이미지 열기
im = Image.open('python.png')  # 스태틱 메서드 (팩토리 함수)

# 이미지 크기 출력(튜플)
print(im.size)

# 이미지 JPG로 저장
im.save('python.jpg')

# 이미지 화면 출력
im.show()

"""
(500, 333)
// png 파일 출력됨
"""

