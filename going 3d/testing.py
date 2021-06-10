import tkinter as Tk
import graphics as g
from Matrix import*
import math
screen=Tk.Tk()

mainCanvas=Tk.Canvas(screen,bg="blue",height=900,width=900)
mainCanvas.pack()

edges=[
g.edge(mainCanvas,[[0,1,1],[1,1,1]]),
g.edge(mainCanvas,[[0,0,1],[0,1,1]]),
g.edge(mainCanvas,[[0,0,1],[1,0,1]]),
g.edge(mainCanvas,[[1,0,1],[1,1,1]]),

g.edge(mainCanvas,[[0,0,1],[0,0,0]]),
g.edge(mainCanvas,[[1,0,1],[1,0,0]]),
g.edge(mainCanvas,[[1,1,1],[1,1,0]]),
g.edge(mainCanvas,[[0,1,1],[0,1,0]]),

g.edge(mainCanvas,[[0,0,0],[1,0,0]]),
g.edge(mainCanvas,[[1,0,0],[1,1,0]]),
g.edge(mainCanvas,[[1,1,0],[0,1,0]]),
g.edge(mainCanvas,[[0,0,0],[0,1,0]])
]




scalar=300
offset=Matrix([[300],[300]])
multiply=Matrix([
    [scalar,0,0],
    [0,0,scalar]
    ])

rscale1=0.01
rscale2=0.01
rscale3=0.01
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
    for x in edges:
        x.transform(rotation1)
        x.transform(rotation2)
        x.transform(rotation3)
    for x in edges:
        x.render(multiply,offset)

    screen.after(10,rotation)
rotation()  


screen.mainloop()


