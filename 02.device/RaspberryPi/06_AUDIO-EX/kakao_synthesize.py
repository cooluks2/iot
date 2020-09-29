import requests
import io
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK 2d7bbeaca71e61a89bef469ece9f01bd"
}
DATA = """
<speak>
    그는 그렇게 말했습니다.
    <voice name="MAN_DIALOG_BRIGHT">잘 지냈어? 나도 잘 지냈어.</voice>
    <voice name="WOMAN_DIALOG_BRIGH">금요일이 좋아요.</voice>
</speak>
"""
res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))

# 음성 합성 결과를 파일로 저장하기
with open("result.mp3", "wb") as f:
  f.write(res.content)

# 바로 재생하기
# https://www.gyan.dev/ffmpeg/builds/
# 환경 변수에 경로 지정
# conda install -c anaconda pyaudio

sound = io.BytesIO(res.content)
song = AudioSegment.from_mp3(sound)

# 파일에서 재생하기
# song = AudioSegment.from_mp3("./result.mp3")
play(song)