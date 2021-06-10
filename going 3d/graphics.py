from Matrix import*
import tkinter as Tk

class point():
    def __init__(self,point=[]):
        self.points=Matrix([[point[0]],[point[1]],[point[2]]])
    def render(self,multiply,offset):

        vectorD=multiply*self.points+offset

        return ([vectorD.Matrix[0][0],vectorD.Matrix[1][0]])
    def transform(self,transform):
        self.points=transform*self.points
        
    def camerapoint(self,camera):
        self.cameraLoc=camera*self.points
    
class edge():
    def __init__(self,master,points=[],**kwargs):
        self.master=master
        self.id= master.create_line(0,50,0,1,width=10,**kwargs)
        self.points=[]
        if len(points)!=2:
            raise ValueError('must have exactly 2 points')
        else:
            for x in points:
                self.points.append(point(x))

    def render(self,multiply,offset):
        points2d=[]
        for x in self.points:
            temp=x.render(multiply,offset)
            points2d.append(temp[0])
            points2d.append(temp[1])
        self.master.coords(self.id,points2d)
        
    def transform(self,transform):
        for x in self.points:
            x.transform(transform)
    def average(self):
        Total=0
        for x in self.points:
            Total+=x.cameraLoc.Matrix[1][0]
        return Total/len(self.points)
    def furthest(self):
        smallest=0
        for x in self.points:
            if smallest>x.cameraLoc.Matrix[1][0]:
                smallest=x.cameraLoc.Matrix[1][0]
        return smallest
    def camerapoint(self,camera):
        for x in self.points:
            x.camerapoint(camera)
    
class face():
    def __init__(self,master,points=[],**kwargs):
        self.master=master
        self.points=[]
        self.id= master.create_polygon([[0,0],[1,1],[1,1]],**kwargs)
        if len(points)<3:
            raise ValueError('must have atleast 3 points')
        else:
            for x in points:
                self.points.append(point(x))
            
    def render(self,multiply,offset):
        points2d=[]
        for x in self.points:
            temp=x.render(multiply,offset)
            points2d.append(temp[0])
            points2d.append(temp[1])
        self.master.coords(self.id,points2d)
    def transform(self,transform):
        for x in self.points:
            x.transform(transform)
    def furthest(self):
        smallest=0
        for x in self.points:
            if smallest>x.cameraLoc.Matrix[1][0]:
                smallest=x.cameraLoc.Matrix[1][0]
        return smallest
    def average(self):
        Total=0
        for x in self.points:
            Total+=x.cameraLoc.Matrix[1][0]
        return Total/len(self.points)
    
    def camerapoint(self,camera):
        for x in self.points:
            x.camerapoint(camera)
            
class item():
    def __init__(self,master,faces=[],edges=[]):
        self.master=master
        self.faces=faces
        self.edges=edges
    def render(self,multiply,offset):
        combined=self.faces.copy()
        combined.extend(self.edges.copy())
        combined.sort(key=lambda x:x.furthest())
        for x in combined:
            self.master.tag_raise(x.id)
        for x in combined:
            x.render(multiply,offset)

    def sceneRender(self,multiply,offset):
        combined=self.faces.copy()
        combined.extend(self.edges)
        for x in combined:
            x.render(multiply,offset)
        return (combined)
    
    def transform(self,transform):
        for x in self.faces:
            x.transform(transform)
        for x in  self.edges:
            x.transform(transform)
    def camerapoint(self,camera):
        for x in self.faces:
            x.camerapoint(camera)
        for x in self.edges:
            x.camerapoint(camera)
            
class axis(item):
    def __init__(self,master):
        self.edges=[
        edge(master,[[0,0,0],[3,0,0]],fill="red"),
        edge(master,[[0,0,0],[0,3,0]],fill="blue"),
        edge(master,[[0,0,0],[0,0,3]],fill="green")
        ]
        item.__init__(self,master,edges=self.edges)
        
        
class box(item):
    def __init__(self,master,point,width,depth,height,colours=["black","black","black","black","black","black"]):
        self.myfaces=[
        face(master,[[point[0],point[1],point[2]],[point[0],point[1]+depth,point[2]],[point[0]+width,point[1]+depth,point[2]],[point[0]+width,point[1],point[2]]],outline="brown",fill=colours[2]),
        face(master,[[point[0],point[1],point[2]],[point[0]+width,point[1],point[2]],[point[0]+width,point[1],point[2]+height],[point[0],point[1],point[2]+height]],outline="brown",fill=colours[5]),
        face(master,[[point[0],point[1],point[2]],[point[0],point[1]+depth,point[2]],[point[0],point[1]+depth,point[2]+height],[point[0],point[1],point[2]+height]],outline="brown",fill=colours[1]),
        face(master,[[point[0],point[1],point[2]+height],[point[0]+width,point[1],point[2]+height],[point[0]+width,point[1]+depth,point[2]+height],[point[0],point[1]+depth,point[2]+height]],outline="brown",fill=colours[4]),
        face(master,[[point[0],point[1]+depth,point[2]],[point[0],point[1]+depth,point[2]+height],[point[0]+width,point[1]+depth,point[2]+height],[point[0]+width,point[1]+depth,point[2]]],outline="brown",fill=colours[0]),
        face(master,[[point[0]+width,point[1],point[2]],[point[0]+width,point[1],point[2]+height],[point[0]+width,point[1]+depth,point[2]+height],[point[0]+width,point[1]+depth,point[2]]],outline="brown",fill=colours[3])]
        item.__init__(self,master,faces=self.myfaces)

        
class scene():
    def __init__(self,master,items):
        self.items=items
        self.master=master
    def render(self,multiply,offset):
        combined=[]
        for x in self.items:
            combined.extend(x.sceneRender(multiply,offset))
        combined.sort(key=lambda x:x.furthest()+x.average())
        for x in combined:
            self.master.tag_raise(x.id)
    def transform(self,transform):
        for x in self.items:
            x.transform(transform)
    def Arender(self,camera,multiply,offset):
        self.camerapoint(camera)
        self.render(multiply*camera,offset)
        
    def camerapoint(self,camera):
        for x in self.items:
            x.camerapoint(camera)

        
    
