import pyaudio
import wave
import io
from pydub import AudioSegment

CHUNK = 1024
FORMAT = pyaudio.paInt16
SAMPLE_WIDTH = 2
CHANNELS = 1
RATE = 44100

def record(record_seconds=5):


    p = pyaudio.PyAudio()
    stream = p.open(input_device_index=0,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start to record the audio.")

    frames = []
    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    print("Recording is finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames


def convertTo16K(file):
    # 16000 으로 변환
    sound = AudioSegment.from_file(file)
    sound = sound.set_frame_rate(16000)
    rec_data = io.BytesIO()
    sound.export
    (rec_data, format="wav")
    return rec_data

# wav 파일 저장
def getWav(frames):
    wavfile = io.BytesIO()
    wf = wave.open(wavfile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wavfile.seek(0)
    return wavfile

if __name__ == "__main__":
    audio_data = record()
    wav_data = getWav(audio_data)
    wav_data = convertTo16K(wav_data)
    # wav_data 처리