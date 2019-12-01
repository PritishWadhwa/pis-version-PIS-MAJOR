from gtts import gTTS
import os

myText = raw_input("Enter text:- ")
output = gTTS(text=myText, lang="en", slow=False)

output.save('output_audio.mp3')
os.system("start output_audio.mp3")
