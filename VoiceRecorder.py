import pyaudio
import wave
from array import array
import random

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 60
SAVE_ADDRESS = "C:\\Users\\Administrator\\Desktop\\Voices"
NAMEE = "RECORDING"
ENDSW = ".mp3"
x = random.randint(0, 100000)
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
frames = []
data = stream.read(CHUNK)
data_chunk = array('h', data)
vol = max(data_chunk)
c = 0
while vol >= -5:

    data = stream.read(CHUNK)
    data_chunk = array('h', data)
    vol = max(data_chunk)
    if(vol >= -20 and len(frames) < 43*RECORD_SECONDS):
        print("something said")
        frames.append(data)
    else:
        if(len(frames) > 43*RECORD_SECONDS):
            c += 1
            print("nothing")
            audio.terminate()
            FILE_NAME = SAVE_ADDRESS+"\\"+NAMEE+str(x)+"-"+str(c)+ENDSW
            wavfile = wave.open(FILE_NAME, 'wb')
            wavfile.setnchannels(CHANNELS)
            wavfile.setsampwidth(audio.get_sample_size(FORMAT))
            wavfile.setframerate(RATE)
            wavfile.writeframes(b''.join(frames))
            wavfile.close()
            frames = []
            audio = pyaudio.PyAudio()
            stream = audio.open(format=FORMAT, channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK)
        else:
            print("nothing")
            frames.append(data)
    print("\n")
stream.stop_stream()
stream.close()
