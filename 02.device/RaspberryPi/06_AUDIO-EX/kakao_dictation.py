import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = '2d7bbeaca71e61a89bef469ece9f01bd'

headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}
with open('heykakao.wav', 'rb') as fp:
    audio = fp.read()

res = requests.post(kakao_speech_url, headers=headers, data=audio)

print(res.text)

result_json_string = res.text[
	res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1
]

result = json.loads(result_json_string)
print(result)
print(result['value'])