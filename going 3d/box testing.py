import tkinter as Tk
import graphics as g
from Matrix import*
import math

import time
screen=Tk.Tk()

mainCanvas=Tk.Canvas(screen,height=900,width=900,bg="orange")
mainCanvas.pack()
O=g.box(mainCanvas,[0,0,0],1,1,1,colours=["white","white","white","white","white","white"])
I=g.box(mainCanvas,[1,1,1],1,1,1,colours=["black","black","black","black","black","black"])

A=g.axis(mainCanvas)
s=g.scene(mainCanvas,[O,I])

#
rscale1=math.radians(-20)#rotate arround red (x)
rscale2=math.radians(-20)#rotate arround blue (y)
rscale3=math.radians(1)#rotate arround green (z)

def rotation1(angle):
    angleR=math.radins(angle)
    return Matrix([
    [1,0,0],
    [0,math.cos(rscale1),-math.sin(rscale1)],
    [0,math.sin(rscale1),math.cos(rscale1)]
    ])

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


s.transform(rotation1)
s.transform(rotation2)
s.transform(rotation3)

def tranform():
    s.transform(rotation3)
    s.render(multiply,offset)
    screen.after(10,tranform)
tranform()

#A.render(multiply,offset)
O.render(multiply,offset)



screen.mainloop()
