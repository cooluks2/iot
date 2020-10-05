import pyaudio
import wave

MIC_DEVICE_ID = 1

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
stream = p.open(input_device_index=MIC_DEVICE_ID,
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

out = p.open(format=FORMAT,
             channels=CHANNELS,
             rate=RATE,
             output=True)

print("Start to record the audio.")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    out.write(data)
    frames.append(data)

print("Recording is finished.")

stream.stop_stream()
stream.close()

p.terminate()
