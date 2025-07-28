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

gender=Combobox(root, values=['Male', 'Female'], font='arial 14', state='readonly', width=10)
gender.place(x=550, y=200)
gender.set('Male')

speed=Combobox(root, values=['Fast', 'Normal', 'Slow'], font='arial 14', state='readonly', width=10)
speed.place(x=730, y=200)
speed.set('Normal')

root.mainloop()