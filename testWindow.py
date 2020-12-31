import tkinter
from tkinter import Button
from playsound import playsound

note_C='resources/sounds/mp3Notes/c3.mp3'

root = tkinter.Tk()

def buttonClick(path):
    playsound(path)
    print("test")

key_C = Button(root,text="click me", command=lambda:buttonClick(note_C))
key_C.pack()

root.mainloop(0)