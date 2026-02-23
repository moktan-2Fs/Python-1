
import speech_recognition as sr
from ollama import chat

recog = sr.Recognizer()


def ask_model(user: str) -> str:
    response = chat(model='llama3.1', messages=[
        {'role': 'user',
                 'content': user}
    ])
    return response.message.content



# userin = input("Want to talk to the my model?(y/n) ").lower()
# if 'y' in userin:
#     user_input_type = input("Want to use voice mode?(y/n): ").strip()
#     if 'y' in user_input_type:
#         while True:
#             try:
#                 with sr.Microphone() as mic:
#                     print("Calibrating noise....")
#                     recog.adjust_for_ambient_noise(mic, duration=2)
#                     print("Say something...I am listening...")
#                     recog.pause_threshold = 2
#                     audio = recog.listen(mic, timeout=5)
#                     text = recog.recognize_tensorflow(audio)
#                     print(text)
#                     rets = ask_model(text)
#                     print(f"You:: {text}\n")
#                     print(f"Model:: {rets}")
#             except sr.UnknownValueError as err:
#                 print(f"Sorry... There was an {err}. Please try again....")
#                 continue
#     else:
#         while True:
#             user_qst = input("\nYou(q to quit):: ").lower()
#             if user_qst == 'q':
#                 break
#             model_res = ask_model(user_qst)
#             print(f"Model:: {model_res}")
