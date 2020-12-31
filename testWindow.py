import tkinter
from tkinter import Button, PhotoImage
from playsound import playsound
import threading

global key
global keyBlack

root = tkinter.Tk()
key = PhotoImage(file='resources/images/key.png')
keyBlack= PhotoImage(file='resources/images/blackKey.png')
def buttonClick(note):
    path = 'resources/sounds/mp3Notes/' + note + '.mp3'
    x = threading.Thread(target=playsound, args=(path,))
    x.start()

key_C = Button(root,image = key, command=lambda:buttonClick("c3"))
key_D = Button(root,image = key, command=lambda:buttonClick("d3"))
key_E = Button(root,image = key, command=lambda:buttonClick("e3"))
key_F = Button(root,image = key, command=lambda:buttonClick("f3"))
key_G = Button(root,image = key, command=lambda:buttonClick("g3"))
key_A = Button(root,image = key, command=lambda:buttonClick("a3"))
key_B = Button(root,image = key, command=lambda:buttonClick("b3"))

key_C.pack(side='left')
key_D.pack(side='left')
key_E.pack(side='left')
key_F.pack(side='left')
key_G.pack(side='left')
key_A.pack(side='left')
key_B.pack(side='left')

key_Black = Button(root,image = keyBlack, command=lambda:buttonClick("c4"))
key_Black.place(x=0,y=0)

root.mainloop(0)