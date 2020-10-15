import cv2
from cam import USBCam
from objdetect import ObjDetectApi

PATH_TO_LABELS = 'data/mscoco_label_map.pbtxt'
MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'

api = ObjDetectApi(MODEL_NAME, PATH_TO_LABELS)

# 영상에 사람이 있는지 여부 판단
def intrusion_detection(output_dict):
    persons = []
    for ix, obj_ix in enumerate(output_dict['detection_classes']):
        if obj_ix == 1 and output_dict['detection_scores'][ix] >= 0.5:
            persons.append(ix)
    
    return len(persons)

def detect(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output_dict = api.inference_image(frame_rgb)

    # 침입인지 아닌지 판단... person ID : 1
    if intrusion_detection(output_dict):
        print("침입 발생")
    # 레코딩 시작.
    # 카톡으로 알림 전송 등 후속 처리 ...

    labeled_image = api.visualize(frame_rgb, output_dict)
    labeled_image = cv2.cvtColor(labeled_image, cv2.COLOR_RGB2BGR)
    cv2.imshow('frame', labeled_image)
    key = cv2.waitKey(1)
    if key == 27:
        return False
    else:
        return True

cam= USBCam()
cam.run(detect)