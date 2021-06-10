import tkinter as Tk
import graphics as g
from Matrix import*
import random
import math

screen=Tk.Tk()
mainCanvas=Tk.Canvas(screen,height=900,width=900,bg="white")
mainCanvas.pack()

cubes=[
g.box(mainCanvas,[-1.5,-1.5,-1.5],1,1,1,colours=["black","green","yellow","black","black","red"]),
g.box(mainCanvas,[-0.5,-1.5,-1.5],1,1,1,colours=["black","black","yellow","black","black","red"]),
g.box(mainCanvas,[0.5,-1.5,-1.5],1,1,1,colours=["black","black","yellow","blue","black","red"]),

g.box(mainCanvas,[-1.5,-0.5,-1.5],1,1,1,colours=["black","green","yellow","black","black","black"]),
g.box(mainCanvas,[-0.5,-0.5,-1.5],1,1,1,colours=["black","black","yellow","black","black","black"]),
g.box(mainCanvas,[0.5,-0.5,-1.5],1,1,1,colours=["black","black","yellow","blue","black","black"]),

g.box(mainCanvas,[-1.5,0.5,-1.5],1,1,1,colours=["orange","green","yellow","black","black","black"]),
g.box(mainCanvas,[-0.5,0.5,-1.5],1,1,1,colours=["orange","black","yellow","black","black","black"]),
g.box(mainCanvas,[0.5,0.5,-1.5],1,1,1,colours=["orange","black","yellow","blue","black","black"]),



g.box(mainCanvas,[-1.5,-1.5,-0.5],1,1,1,colours=["black","green","black","black","black","red"]),
g.box(mainCanvas,[-0.5,-1.5,-0.5],1,1,1,colours=["black","black","black","black","black","red"]),
g.box(mainCanvas,[0.5,-1.5,-0.5],1,1,1,colours=["black","black","black","blue","black","red"]),

g.box(mainCanvas,[-1.5,-0.5,-0.5],1,1,1,colours=["black","green","black","black","black","black"]),
g.box(mainCanvas,[-0.5,-0.5,-0.5],1,1,1,colours=["black","black","black","black","black","black"]),
g.box(mainCanvas,[0.5,-0.5,-0.5],1,1,1,colours=["black","black","black","blue","black","black"]),

g.box(mainCanvas,[-1.5,0.5,-0.5],1,1,1,colours=["orange","green","black","black","black","black"]),
g.box(mainCanvas,[-0.5,0.5,-0.5],1,1,1,colours=["orange","black","black","black","black","black"]),
g.box(mainCanvas,[0.5,0.5,-0.5],1,1,1,colours=["orange","black","black","blue","black","black"]),


g.box(mainCanvas,[-1.5,-1.5,0.5],1,1,1,colours=["black","green","black","black","white","red"]),
g.box(mainCanvas,[-0.5,-1.5,0.5],1,1,1,colours=["black","black","black","black","white","red"]),
g.box(mainCanvas,[0.5,-1.5,0.5],1,1,1,colours=["black","black","black","blue","white","red"]),

g.box(mainCanvas,[-1.5,-0.5,0.5],1,1,1,colours=["black","green","black","black","white","black"]),
g.box(mainCanvas,[-0.5,-0.5,0.5],1,1,1,colours=["black","black","black","black","white","black"]),
g.box(mainCanvas,[0.5,-0.5,0.5],1,1,1,colours=["black","black","black","blue","white","black"]),

g.box(mainCanvas,[-1.5,0.5,0.5],1,1,1,colours=["orange","green","black","black","white","black"]),
g.box(mainCanvas,[-0.5,0.5,0.5],1,1,1,colours=["orange","black","black","black","white","black"]),
g.box(mainCanvas,[0.5,0.5,0.5],1,1,1,colours=["orange","black","black","blue","white","black"]),
]
s=g.scene(mainCanvas,cubes)
scalar=150
offset=Matrix([[450],[450]])
multiply=Matrix([
    [scalar,0,0],
    [0,0,scalar]
    ])

camera=Matrix([[1,0,0],[0,1,0],[0,0,1]])

cube=[
    [0,1,2,3,4,5,6,7,8],
    [9,10,11,12,13,14,15,16,17],
    [18,19,20,21,22,23,24,25,26]
]

scale=math.radians(3)
count=30

def rotate(Rcube,matrix,number):
    for x in Rcube:
        cubes[x].transform(matrix)
    s.Arender(camera,multiply,offset)
    mainCanvas.update_idletasks()
    if number>1:
        screen.after(1,rotate(Rcube,matrix,number-1))


    
def Rleft(key):
    global camera
    scale=math.radians(1)
    rotationMatrix=Matrix([[math.cos(scale),-math.sin(scale),0],[math.sin(scale),math.cos(scale),0],[0,0,1]])
    camera=rotationMatrix*camera
    s.Arender(camera,multiply,offset)
def RRight(key):
    global camera
    scale=math.radians(-1)
    rotationMatrix=Matrix([[math.cos(scale),-math.sin(scale),0],[math.sin(scale),math.cos(scale),0],[0,0,1]])
    camera=rotationMatrix*camera
    s.Arender(camera,multiply,offset)
def Rup(key):
    global camera
    scale=math.radians(1)
    rotationMatrix=Matrix([[1,0,0],[0,math.cos(scale),-math.sin(scale)],[0,math.sin(scale),math.cos(scale)]])
    camera=rotationMatrix*camera
    s.Arender(camera,multiply,offset)
def Rdown(key):
    global camera
    scale=math.radians(-1)
    rotationMatrix=Matrix([[1,0,0],[0,math.cos(scale),-math.sin(scale)],[0,math.sin(scale),math.cos(scale)]])
    camera=rotationMatrix*camera
    s.Arender(camera,multiply,offset)

def Ry(key):
    yelow=cube[0]
    scale=math.radians(3)
    rotate(yelow,Matrix([[math.cos(scale),-math.sin(scale),0],[math.sin(scale),math.cos(scale),0],[0,0,1]]),count)
    temp=[]
    for x in cube:
        temp.append(x[:])
    cube[0][2]=temp[0][0]
    cube[0][5]=temp[0][1]
    cube[0][8]=temp[0][2]
    cube[0][1]=temp[0][3]
    cube[0][7]=temp[0][5]
    cube[0][0]=temp[0][6]
    cube[0][3]=temp[0][7]
    cube[0][6]=temp[0][8]
    
def Rg(key):
    green=[]
    row1=[0,3,6]
    row2=[0,1,2]
    for x in row1:
        for y in row2:
            green.append(cube[y][x])
    rotate(green,Matrix([[1,0,0],[0,math.cos(scale),-math.sin(scale)],[0,math.sin(scale),math.cos(scale)]]),count)
    temp=[]
    for x in cube:
        temp.append(x[:])
    cube[0][6]=temp[0][0]
    cube[1][6]=temp[0][3]
    cube[2][6]=temp[0][6]
    cube[0][3]=temp[1][0]
    cube[2][3]=temp[1][6]
    cube[0][0]=temp[2][0]
    cube[1][0]=temp[2][3]
    cube[2][0]=temp[2][6]
    
def Ro(key):
    orange=[]
    row1=[6,7,8]
    row2=[0,1,2]
    for x in row1:
        for y in row2:
            orange.append(cube[y][x])
    rotate(orange,Matrix([[math.cos(scale),0,math.sin(scale)],[0,1,0],[-math.sin(scale),0,math.cos(scale)]]),count)
    temp=[]
    for x in cube:
        temp.append(x[:])
    cube[2][6]=temp[0][6]
    cube[1][6]=temp[0][7]
    cube[0][6]=temp[0][8]
    cube[2][7]=temp[1][6]
    cube[0][7]=temp[1][8]
    cube[2][8]=temp[2][6]
    cube[1][8]=temp[2][7]
    cube[0][8]=temp[2][8]
    
def Rb(key):
    blue=[]
    row1=[2,5,8]
    row2=[0,1,2]
    for x in row1:
        for y in row2:
            blue.append(cube[y][x])
    rotate(blue,Matrix([[1,0,0],[0,math.cos(scale),-math.sin(scale)],[0,math.sin(scale),math.cos(scale)]]),count)
    temp=[]
    for x in cube:
        temp.append(x[:])
    cube[0][8]=temp[0][2]
    cube[1][8]=temp[0][5]
    cube[2][8]=temp[0][8]
    cube[0][5]=temp[1][2]
    cube[2][5]=temp[1][8]
    cube[0][2]=temp[2][2]
    cube[1][2]=temp[2][5]
    cube[2][2]=temp[2][8]
    
def Rr(key):
    red=[]
    row1=[0,1,2]
    row2=[0,1,2]
    for x in row1:
        for y in row2:
            red.append(cube[y][x])
    rotate(red,Matrix([[math.cos(scale),0,math.sin(scale)],[0,1,0],[-math.sin(scale),0,math.cos(scale)]]),count)
    temp=[]
    for x in cube:
        temp.append(x[:])
    cube[2][0]=temp[0][0]
    cube[1][0]=temp[0][1]
    cube[0][0]=temp[0][2]
    cube[2][1]=temp[1][0]
    cube[0][1]=temp[1][2]
    cube[2][2]=temp[2][0]
    cube[1][2]=temp[2][1]
    cube[0][2]=temp[2][2]
    
def Rw(key):
    white=cube[2]
    rotate(white,Matrix([[math.cos(scale),-math.sin(scale),0],[math.sin(scale),math.cos(scale),0],[0,0,1]]),count)
    temp=[]
    for x in cube:
        temp.append(x[:])
    cube[2][2]=temp[2][0]
    cube[2][5]=temp[2][1]
    cube[2][8]=temp[2][2]
    cube[2][1]=temp[2][3]
    cube[2][7]=temp[2][5]
    cube[2][0]=temp[2][6]
    cube[2][3]=temp[2][7]
    cube[2][6]=temp[2][8]

screen.bind("<Up>",Rup)
screen.bind("<Down>",Rdown)
screen.bind("<Left>",Rleft)
screen.bind("<Right>",RRight)

screen.bind("q",Ry)
screen.bind("w",Rg)
screen.bind("e",Ro)
screen.bind("r",Rb)
screen.bind("t",Rr)
screen.bind("y",Rw)

s.Arender(camera,multiply,offset)

def shuffle(key):
    a=random.randint(0,6)
    if a == 0:
        screen.after(1,Ry(a))
    elif a == 1:
        screen.after(1,Rg(a))
    elif a == 2:
        screen.after(1,Ro(a))
    elif a == 3:
        screen.after(1,Rb(a))
    elif a == 4:
        screen.after(1,Rr(a))
    elif a == 5:
        screen.after(1,Rw(a))
s.Arender(camera,multiply,offset)
screen.bind("<space>",shuffle)
screen.mainloop()

