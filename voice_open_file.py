from mysource import voice_to_text
import os
import pathlib
import platform
import speech_recognition as sr

speech = sr.Recognizer()
directory = pathlib.Path.cwd()


# function to convert voice to text
inp = voice_to_text()


# function to open a file
def open_file(filename):
    if platform.system() == "Windows":
        os.system(f"explorer {directory}\\files\\{filename}")
    elif platform.system() == "Darwin":
        os.system(f"open {directory}/files/{filename}")
    else:
        os.system(f"xdg-open {directory}/files/{filename}")


while True:
    print("python is listening....")
    inp = voice_to_text().lower()
    print(f'You just said {inp}.')
    if inp == "stop listening":
        print('Goodbye!')
        break
    elif "open pdf" in inp:
        inp = inp.replace('open pdf ', '')
        myfile = f'{inp}.pdf'
        open_file(myfile)
        continue
    elif "open word" in inp:
        inp = inp.replace('open word ', '')
        myfile = f'{inp}.docx'
        open_file(myfile)
        continue
    elif "open excel" in inp:
        inp = inp.replace('open excel ', '')
        myfile = f'{inp}.xlsx'
        open_file(myfile)
        continue
    elif "open powerpoint" in inp:
        inp = inp.replace('open powerpoint ', '')
        myfile = f'{inp}.pptx'
        open_file(myfile)
        continue
    elif "open audio" in inp:
        inp = inp.replace('open audio ', '')
        myfile = f'{inp}.mp3'
        open_file(myfile)
        continue
    elif "open txt" in inp:
        inp = inp.replace('open txt ', '')
        myfile = f'{inp}.txt'
        open_file(myfile)
        continue