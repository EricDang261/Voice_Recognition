import speech_recognition as sr
from mysource import voice_to_text

speech = sr.Recognizer()
while True:
    print('Python is listening...')
    inp = voice_to_text()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print("Good bye")
        break
