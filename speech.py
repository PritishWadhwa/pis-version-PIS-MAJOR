import time
import speech_recognition as sr
def speech2text():
    r = sr.Recognizer()

    while 1:
        with sr.Microphone(device_index=2) as src:
            print("Say Something")
            try:            
                audio = r.listen(src,timeout=4)
                text = r.recognize_google(audio,language = "en-IN")
                print("You said: {0} ".format(text))
                #yield text
            #except sr.UnknownValueError:
             #   print "Going to sleep"
              #  time.sleep(10)
            except Exception as e:
                #raise(e) 
                print("Could not understand what you said")

speech2text()
if __name__ == "__main__":
    print "in"
    speech2text()
