from django import forms
import json
import requests

class KaKaoTalkForm(forms.Form):
    text = forms.CharField(label='전송할 Talk', max_length=300)
    web_url = forms.CharField(label='Web URL', max_length=300,
                        initial='http://192.168.0.10:8000/mjpeg?mode=stream')
    mobile_web_url = forms.CharField(label='Mobile Url', max_length=300,
                        initial='http://192.168.0.10:8000/mjpeg?mode=stream')

    def send_talk(self):
        talk_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        with open("access_token.txt", "r") as f:
            token = f.read()

        header = {"Authorization": f"Bearer {token}"}
        text_template = {
            "object_type": "location",
            "address" : "서울시 성북구 보문로 13다길 30",
            "content": {
                "title": "달 사진",
                "description": "위치보기는 집으로",
                "image_url": "https://www.thisiscolossal.com/wp-content/uploads/2019/02/moon_crop-640x640.jpg",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
        }
        print(text_template)
        payload = {'template_object': json.dumps(text_template)}
        res = requests.post(talk_url, data=payload, headers=header)

        return res, self.cleaned_data['text']
