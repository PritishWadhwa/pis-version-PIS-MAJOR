import speech_recognition as sr
import sys
from datetime import datetime

print("Start-Time: ",datetime.now())
r = sr.Recognizer()
audio_file = "wav_file.wav"
with sr.AudioFile(audio_file) as src:
    print("inside with block")
    audio = r.record(src)
    print("audio-recorded")
try:
    print("inside try")
    text = r.recognize_google(audio)
    print("You said: {0} ".format(text))
except Exception as e:
    print("Could not understand what you said")

print("End-Time: ",datetime.now())

