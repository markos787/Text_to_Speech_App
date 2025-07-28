import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3
import os

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
button_speak=Button(root, text='SPEAK', compound=LEFT, image=speak_icon, width=140, font='arial 16 bold', command=speaking)
button_speak.place(x=550, y=280)

download_icon=PhotoImage(file='icons\\download.png')
button_download=Button(root, text='SAVE', compound=LEFT, image=download_icon, bg='#39c790', width=140, font='arial 16 bold', command=saving)
button_download.place(x=730, y=280)

root.mainloop()