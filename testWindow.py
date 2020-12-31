import tkinter
from tkinter import Button
from playsound import playsound

note_C='resources/sounds/mp3Notes/c3.mp3'
note_D='resources/sounds/mp3Notes/d3.mp3'
note_E='resources/sounds/mp3Notes/e3.mp3'
note_F='resources/sounds/mp3Notes/f3.mp3'
note_G='resources/sounds/mp3Notes/g3.mp3'
note_A='resources/sounds/mp3Notes/a3.mp3'
note_B='resources/sounds/mp3Notes/b3.mp3'

root = tkinter.Tk()

def buttonClick(path):
    playsound(path)

key_C = Button(root,text="C3", command=lambda:buttonClick(note_C))
key_D = Button(root,text="D3", command=lambda:buttonClick(note_D))
key_E = Button(root,text="E3", command=lambda:buttonClick(note_E))
key_F = Button(root,text="F3", command=lambda:buttonClick(note_F))
key_G = Button(root,text="G3", command=lambda:buttonClick(note_G))
key_A = Button(root,text="A3", command=lambda:buttonClick(note_A))
key_B = Button(root,text="B3", command=lambda:buttonClick(note_B))

key_C.pack()
key_D.pack()
key_E.pack()
key_F.pack()
key_G.pack()
key_A.pack()
key_B.pack()

root.mainloop(0)