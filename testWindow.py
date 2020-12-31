import tkinter
from tkinter import Button, PhotoImage
from playsound import playsound

global key

note_C='resources/sounds/mp3Notes/c3.mp3'
note_D='resources/sounds/mp3Notes/d3.mp3'
note_E='resources/sounds/mp3Notes/e3.mp3'
note_F='resources/sounds/mp3Notes/f3.mp3'
note_G='resources/sounds/mp3Notes/g3.mp3'
note_A='resources/sounds/mp3Notes/a3.mp3'
note_B='resources/sounds/mp3Notes/b3.mp3'


root = tkinter.Tk()
key = PhotoImage(file='resources/images/key.png')
def buttonClick(path):
    playsound(path)

key_C = Button(root,image = key, command=lambda:buttonClick(note_C))
key_D = Button(root,image = key, command=lambda:buttonClick(note_D))
key_E = Button(root,image = key, command=lambda:buttonClick(note_E))
key_F = Button(root,image = key, command=lambda:buttonClick(note_F))
key_G = Button(root,image = key, command=lambda:buttonClick(note_G))
key_A = Button(root,image = key, command=lambda:buttonClick(note_A))
key_B = Button(root,image = key, command=lambda:buttonClick(note_B))

key_C.pack(side='left')
key_D.pack(side='left')
key_E.pack(side='left')
key_F.pack(side='left')
key_G.pack(side='left')
key_A.pack(side='left')
key_B.pack(side='left')

root.mainloop(0)