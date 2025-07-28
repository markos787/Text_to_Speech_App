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

root.mainloop()

# Film przerwany na: 9:50