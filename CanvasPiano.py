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

canvas.tag_bind(c4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/c4.mp3'))
canvas.tag_bind(d4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/d4.mp3'))
canvas.tag_bind(e4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/e4.mp3'))
canvas.tag_bind(f4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/f4.mp3'))
canvas.tag_bind(g4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/g4.mp3'))
canvas.tag_bind(cs4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/c-4.mp3'))
canvas.tag_bind(ds4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/d-4.mp3'))
canvas.tag_bind(fs4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/f-4.mp3'))

root.mainloop()