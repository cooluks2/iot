# 20200721094050-001.jpg 파일 10개 만들기
# 내 풀이
import time

for a in range(1, 11):
    print(time.strftime('%Y%m%d%I%M%S'), end="")
    print(f"-{a:03d}", end="")
    print(".jpg")


# 강사님

import time
from datetime import datetime
now = datetime.now()

for i in range(1, 11):
    fname = now.strftime(f"%Y%m%d%H%M%S-{i:03d}.jpg")  # 3자리 차지, 빈자리0
    print(fname)


"""
20200721095428-001.jpg
20200721095428-002.jpg
20200721095428-003.jpg
20200721095428-004.jpg
20200721095428-005.jpg
20200721095428-006.jpg
20200721095428-007.jpg
20200721095428-008.jpg
20200721095428-009.jpg
20200721095428-010.jpg
"""