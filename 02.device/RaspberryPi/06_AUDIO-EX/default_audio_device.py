import pyaudio

p = pyaudio.PyAudio()

default_input = p.get_default_input_device_info()
print(default_input)

default_output = p.get_default_output_device_info()
print(default_output)