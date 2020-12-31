from tkinter import *
import winsound
from playsound import playsound
import threading

sound_C3='resources/sounds/mp3Notes/c3.mp3'

def playnote(event, path):
    buttonClick(path)

def buttonClick(event, path):
    x = threading.Thread(target=playsound,args=(path,))
    x.start()
    print('testing')
#from winsound import *


# winsound.Beep('frequency', 'duration')
def playc4(event):
    print("C4!")
    winsound.Beep(262, 500)

def playcs4(event):
    print("C#4!")
    winsound.Beep(277, 500)

def playd4(event):
    print("D4!")
    winsound.Beep(294, 500)

def playds4(event):
    print("D#4!")
    winsound.Beep(311, 500)

def playe4(event):
    print("E4!")
    winsound.Beep(330, 500)

def playf4(event):
    print("F4!")
    winsound.Beep(349, 500)

def playfs4(event):
    print("F#4!")
    winsound.Beep(370, 500)

def playg4(event):
    print("G4!")
    winsound.Beep(392, 500)


root = Tk()

canvas = Canvas(root, height=300, width=1200)
canvas.pack()

# testrectangle = canvas.create_rectangle(0, 0, 50, 100, fill="purple")
c4 = canvas.create_polygon(0, 0, 0, 300, 50, 300, 50, 0, fill='gainsboro', outline='light steel blue')
d4 = canvas.create_polygon(50, 0, 50, 300, 100, 300, 100, 0, fill='gainsboro', outline='light steel blue')
e4 = canvas.create_polygon(100, 0, 100, 300, 150, 300, 150, 0, fill='gainsboro', outline='light steel blue')
f4 = canvas.create_polygon(150, 0, 150, 300, 200, 300, 200, 0, fill='gainsboro', outline='light steel blue')
g4 = canvas.create_polygon(200, 0, 200, 300, 250, 300, 250, 0, fill='gainsboro', outline='light steel blue')

cs4 = canvas.create_polygon(35, 0, 35, 200, 65, 200, 65, 0, fill='black')
ds4 = canvas.create_polygon(85, 0, 85, 200, 115, 200, 115, 0, fill='black')
fs4 = canvas.create_polygon(185, 0, 185, 200, 215, 200, 215, 0, fill='black')

canvas.tag_bind(c4, "<Button-1>", lambda event: buttonClick(event, path=sound_C3))
canvas.tag_bind(d4, "<Button-1>", playd4)
canvas.tag_bind(e4, "<Button-1>", playe4)
canvas.tag_bind(f4, "<Button-1>", playf4)
canvas.tag_bind(g4, "<Button-1>", playg4)
canvas.tag_bind(cs4, "<Button-1>", playcs4)
canvas.tag_bind(ds4, "<Button-1>", playds4)
canvas.tag_bind(fs4, "<Button-1>", playfs4)

root.mainloop()