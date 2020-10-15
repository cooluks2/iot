import cv2
import pathlib
from objdetect import ObjDetectApi

PATH_TO_LABELS = 'data/mscoco_label_map.pbtxt'
MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
api = ObjDetectApi(MODEL_NAME, PATH_TO_LABELS)

# 예제 데이터
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('test_images')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))

# 검출 진행
for image_path in TEST_IMAGE_PATHS:
    image, output_dict = api.inference_file(image_path)
    print(output_dict)
    labeled_image = api.visualize(image, output_dict)
    labeled_image = cv2.cvtColor(labeled_image, cv2.COLOR_RGB2BGR)
    cv2.imshow('image', labeled_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()