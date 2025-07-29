import tkinter as tk
import pyttsx3
import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from pathlib import Path


def speaking():
    engine=pyttsx3.init() # pyttsx3 converts text to speech - main factor of the application
    text_var=text_input.get(1.0, END) # 1.0 means from the beginning, to the END
    gender_var=gender.get()
    speed_var=speed.get()
    voices=engine.getProperty('voices')

    def set_voice():
        if gender_var=='Male':
            engine.setProperty('voice', voices[0].id) # 0 - Male
        else:
            engine.setProperty('voice', voices[1].id) # 1 - Female
    
    if text_var:
        if speed_var=='Fast':
            engine.setProperty('rate', 250)
        elif speed_var=='Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)

        set_voice()
        engine.say(text=text_var)
        engine.runAndWait()
        engine.stop()

def saving():
    engine=pyttsx3.init() # pyttsx3 converts text to speech - main factor of the application
    text_var=text_input.get(1.0, END)
    gender_var=gender.get()
    speed_var=speed.get()
    voices=engine.getProperty('voices')

    def set_voice():
        if gender_var=='Male':
            engine.setProperty('voice', voices[0].id) # 0 - Male
        else:
            engine.setProperty('voice', voices[1].id) # 1 - Female

        path=Path(filedialog.asksaveasfilename(defaultextension='.mp3', filetypes=[('MP3 Files', '*.mp3')])) # asks for directory and filename
        file_name=path.name
        folder_path=path.parent
        os.chdir(path=folder_path)
        engine.save_to_file(text_var, file_name)
        engine.runAndWait()
        engine.stop()
    
    if text_var:
        if speed_var=='Fast':
            engine.setProperty('rate', 250)
        elif speed_var=='Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)

        set_voice()


root=Tk()
root.title('Text to Speech')
root.geometry('900x450+500+300')
root.resizable(False, False)
root.configure(bg='#305065')

# Icon
icon_img=PhotoImage(file='icons\\speak.png')
root.iconphoto(False, icon_img) # False - icon won't be inheritated by child windows

# Top frame
frame_top=Frame(root, bg='white', width=900, height=100)
frame_top.place(x=0, y=0)

logo=PhotoImage(file='icons\\speaker logo.png')
Label(frame_top, image=logo, bg='white').place(x=10, y=5)

Label(frame_top, text='TEXT TO SPEECH',font='arial 20 bold', bg='white', fg='black').place(x=100, y=35)

# Parameters
text_input=Text(root, font='Robote 20', bg='white', relief=GROOVE, wrap=WORD) # relief - bordering (GROOVE - slightly 3D frame), WORD - wrapping all words
text_input.place(x=20, y=150, width=500, height=250)

Label(root, text='VOICE', font='arial 14 bold', bg='#305065', fg='white').place(x=580, y=170)
gender=Combobox(root, values=['Male', 'Female'], font='arial 14', state='readonly', width=10)
gender.place(x=550, y=200)
gender.set('Male')

Label(root, text='SPEED', font='arial 14 bold', bg='#305065', fg='white').place(x=757, y=170)
speed=Combobox(root, values=['Fast', 'Normal', 'Slow'], font='arial 14', state='readonly', width=10)
speed.place(x=730, y=200)
speed.set('Normal')

speak_icon=PhotoImage(file='icons\\speak.png')
button_speak=Button(root, text='SPEAK', compound=LEFT, image=speak_icon, width=130, font='arial 16 bold', command=speaking)
button_speak.place(x=550, y=280)

download_icon=PhotoImage(file='icons\\download.png')
button_download=Button(root, text='SAVE', compound=LEFT, image=download_icon, bg='#39c790', width=130, font='arial 16 bold', command=saving)
button_download.place(x=730, y=280)

root.mainloop()