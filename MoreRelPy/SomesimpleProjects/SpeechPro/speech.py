# the most impotant functions of speechrecognition are:
#  listen() -> captures audio from mic
# common parameters of listen() are:
# (source, timeout=5, wait time to start speaking
# pharse_time_limit = 10) max speech duration
#
#
#
# ##

import speech_recognition

recogn = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Calibrating noise....")
            recogn.adjust_for_ambient_noise(mic, duration=1)
            print("Say something...I am listening..")
            recogn.pause_threshold = 2
            audio = recogn.listen(mic, timeout=5)
            text = recogn.recognize_google(audio)
            print(text)
            stop = input("Stop?(y/n): ").lower()
    except speech_recognition.UnknownValueError and speech_recognition.WaitTimeoutError:
        recogn = speech_recognition.Recognizer()
        continue
    if "y" in stop:
        break

# with speech_recognition.AudioFile('./ontheflip.mp3') as source:
#     audio = recogn.record(source)
