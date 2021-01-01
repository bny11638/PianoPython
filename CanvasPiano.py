from tkinter import *
import winsound
from playsound import playsound
import threading

sound_C3='resources/sounds/mp3Notes/c3.mp3'


def buttonClick(event, path):
    x = threading.Thread(target=playsound,args=(path,))
    x.start()
    print('testing')
#from winsound import *


# winsound.Beep('frequency', 'duration')



root = Tk()

canvas = Canvas(root, height=300, width=1100)

canvas.bind("<1>", lambda event: canvas.focus_set())
canvas.pack()

# testrectangle = canvas.create_rectangle(0, 0, 50, 100, fill="purple")
# Initialize white keys
c3 = canvas.create_polygon(0, 0, 0, 300, 50, 300, 50, 0, fill='gainsboro', outline='light steel blue')
d3 = canvas.create_polygon(50, 0, 50, 300, 100, 300, 100, 0, fill='gainsboro', outline='light steel blue')
e3 = canvas.create_polygon(100, 0, 100, 300, 150, 300, 150, 0, fill='gainsboro', outline='light steel blue')
f3 = canvas.create_polygon(150, 0, 150, 300, 200, 300, 200, 0, fill='gainsboro', outline='light steel blue')
g3 = canvas.create_polygon(200, 0, 200, 300, 250, 300, 250, 0, fill='gainsboro', outline='light steel blue')
a3 = canvas.create_polygon(250, 0, 250, 300, 300, 300, 300, 0, fill='gainsboro', outline='light steel blue')
b3 = canvas.create_polygon(300, 0, 300, 300, 350, 300, 350, 0, fill='gainsboro', outline='light steel blue')
c4 = canvas.create_polygon(350, 0, 350, 300, 400, 300, 400, 0, fill='gainsboro', outline='light steel blue')
d4 = canvas.create_polygon(400, 0, 400, 300, 450, 300, 450, 0, fill='gainsboro', outline='light steel blue')
e4 = canvas.create_polygon(450, 0, 450, 300, 500, 300, 500, 0, fill='gainsboro', outline='light steel blue')
f4 = canvas.create_polygon(500, 0, 500, 300, 550, 300, 550, 0, fill='gainsboro', outline='light steel blue')
g4 = canvas.create_polygon(550, 0, 550, 300, 600, 300, 600, 0, fill='gainsboro', outline='light steel blue')
a4 = canvas.create_polygon(600, 0, 600, 300, 650, 300, 650, 0, fill='gainsboro', outline='light steel blue')
b4 = canvas.create_polygon(650, 0, 650, 300, 700, 300, 700, 0, fill='gainsboro', outline='light steel blue')
c5 = canvas.create_polygon(700, 0, 700, 300, 750, 300, 750, 0, fill='gainsboro', outline='light steel blue')
d5 = canvas.create_polygon(750, 0, 750, 300, 800, 300, 800, 0, fill='gainsboro', outline='light steel blue')
e5 = canvas.create_polygon(800, 0, 800, 300, 850, 300, 850, 0, fill='gainsboro', outline='light steel blue')
f5 = canvas.create_polygon(850, 0, 850, 300, 900, 300, 900, 0, fill='gainsboro', outline='light steel blue')
g5 = canvas.create_polygon(900, 0, 900, 300, 950, 300, 950, 0, fill='gainsboro', outline='light steel blue')
a5 = canvas.create_polygon(950, 0, 950, 300, 1000, 300, 1000, 0, fill='gainsboro', outline='light steel blue')
b5 = canvas.create_polygon(1000, 0, 1000, 300, 1050, 300, 1050, 0, fill='gainsboro', outline='light steel blue')
c6 = canvas.create_polygon(1050, 0, 1050, 300, 1100, 300, 1100, 0, fill='gainsboro', outline='light steel blue')


"""
c4 = canvas.create_polygon(0, 0, 0, 300, 50, 300, 50, 0, fill='gainsboro', outline='light steel blue')
d4 = canvas.create_polygon(50, 0, 50, 300, 100, 300, 100, 0, fill='gainsboro', outline='light steel blue')
e4 = canvas.create_polygon(100, 0, 100, 300, 150, 300, 150, 0, fill='gainsboro', outline='light steel blue')
f4 = canvas.create_polygon(150, 0, 150, 300, 200, 300, 200, 0, fill='gainsboro', outline='light steel blue')
g4 = canvas.create_polygon(200, 0, 200, 300, 250, 300, 250, 0, fill='gainsboro', outline='light steel blue')
"""

as3 = canvas.create_polygon(35, 0, 35, 200, 65, 200, 65, 0, fill='black')
cs4 = canvas.create_polygon(135, 0, 135, 200, 165, 200, 165, 0, fill='black')
ds4 = canvas.create_polygon(185, 0, 185, 200, 215, 200, 215, 0, fill='black')
fs4 = canvas.create_polygon(285, 0, 285, 200, 315, 200, 315, 0, fill='black')
gs4 = canvas.create_polygon(335, 0, 335, 200, 365, 200, 365, 0, fill='black')
as4 = canvas.create_polygon(385, 0, 385, 200, 415, 200, 415, 0, fill='black')
cs5 = canvas.create_polygon(485, 0, 485, 200, 515, 200, 515, 0, fill='black')
ds5 = canvas.create_polygon(535, 0, 535, 200, 565, 200, 565, 0, fill='black')
fs5 = canvas.create_polygon(635, 0, 635, 200, 665, 200, 665, 0, fill='black')
gs5 = canvas.create_polygon(685, 0, 685, 200, 715, 200, 715, 0, fill='black')
as5 = canvas.create_polygon(735, 0, 735, 200, 765, 200, 765, 0, fill='black')


"""
cs4 = canvas.create_polygon(35, 0, 35, 200, 65, 200, 65, 0, fill='black')
ds4 = canvas.create_polygon(85, 0, 85, 200, 115, 200, 115, 0, fill='black')
fs4 = canvas.create_polygon(185, 0, 185, 200, 215, 200, 215, 0, fill='black')
"""

# canvas.tag_bind(f4, "<Return>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/f4.mp3'))

canvas.tag_bind(c3, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/c3.mp3'))
canvas.tag_bind(d3, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/d3.mp3'))
canvas.tag_bind(e3, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/e3.mp3'))
canvas.tag_bind(f3, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/f3.mp3'))
canvas.tag_bind(g3, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/g3.mp3'))
canvas.tag_bind(a3, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/a4.mp3'))
canvas.tag_bind(b3, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/b4.mp3'))
canvas.tag_bind(c4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/c4.mp3'))
canvas.tag_bind(d4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/d4.mp3'))
canvas.tag_bind(e4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/e4.mp3'))
canvas.tag_bind(f4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/f4.mp3'))
canvas.tag_bind(g4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/g4.mp3'))
canvas.tag_bind(a4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/a5.mp3'))
canvas.tag_bind(b4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/b5.mp3'))
canvas.tag_bind(c5, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/c5.mp3'))
canvas.tag_bind(d5, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/d5.mp3'))
canvas.tag_bind(e5, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/e5.mp3'))
canvas.tag_bind(f5, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/f5.mp3'))
canvas.tag_bind(g5, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/g5.mp3'))
canvas.tag_bind(a5, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/a5.mp3'))
canvas.tag_bind(b5, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/b5.mp3'))
canvas.tag_bind(c6, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/c6.mp3'))



canvas.tag_bind(as4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/a-4.mp3'))

"""
canvas.tag_bind(cs4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/c-4.mp3'))
canvas.tag_bind(ds4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/d-4.mp3'))
canvas.tag_bind(fs4, "<Button-1>", lambda event: buttonClick(event, path='resources/sounds/mp3Notes/f-4.mp3'))
"""


root.mainloop()