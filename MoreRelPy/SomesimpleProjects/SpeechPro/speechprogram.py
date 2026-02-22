from datetime import datetime, time , date
import speech_recognition as sr 

recog = sr.Recognizer()
def speech_to_text(a):
    try:
        with sr.Microphone() as source:
            recog.adjust_for_ambient_noise(source, duration= 10)
            audio = recog.listen(source, timeout=10)
            text = recog.recognize_google(audio)
            return text 
    except sr.UnknownValueError as uk:
        print(f"There was {uk}.")