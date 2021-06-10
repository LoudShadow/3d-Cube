import tkinter as Tk
import graphics as g
from Matrix import*
import math

import time
screen=Tk.Tk()

mainCanvas=Tk.Canvas(screen,bg="blue",height=900,width=900)
mainCanvas.pack()

faces=[
g.face(mainCanvas,[[0,0,1],[0,1,1],[1,1,1],[1,0,1]],fill="red"),
g.face(mainCanvas,[[0,0,1],[1,0,1],[1,0,0],[0,0,0]],fill="yellow"),
g.face(mainCanvas,[[0,0,1],[0,1,1],[0,1,0],[0,0,0]],fill="green"),
g.face(mainCanvas,[[0,1,1],[1,1,1],[1,1,0],[0,1,0]],fill="orange"),
g.face(mainCanvas,[[1,0,1],[1,1,1],[1,1,0],[1,0,0]],fill="black"),
g.face(mainCanvas,[[0,0,0],[0,1,0],[1,1,0],[1,0,0]],fill="white"),
]

O=g.item(mainCanvas,faces=faces)

scalar=300
offset=Matrix([[300],[300]])
multiply=Matrix([
    [scalar,0,0],
    [0,0,scalar]
    ])

rscale1=math.radians(1)
rscale2=math.radians(1)
rscale3=math.radians(1)
rotation1=Matrix([
    [1,0,0],
    [0,math.cos(rscale1),-math.sin(rscale1)],
    [0,math.sin(rscale1),math.cos(rscale1)]
    ])

rotation2=Matrix([
    [math.cos(rscale2),0,math.sin(rscale2)],
    [0,1,0],
    [-math.sin(rscale2),0,math.cos(rscale2)]
    ])

rotation3=Matrix([
    [math.cos(rscale3),-math.sin(rscale3),0],
    [math.sin(rscale3),math.cos(rscale3),0],
    [0,0,1]
    ])

def rotation():
    O.transform(rotation1)
    O.transform(rotation2)
    O.transform(rotation3)
    O.render(multiply,offset)
    screen.after(10,rotation)
rotation()  


screen.mainloop()
