# Draws World

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
pygame.init()

from objLoader import *

from Cube import *
from Plane import *
from Wall import *
from Texture import *

class World(object):
    def __init__(self):
        print "World Initialised."
        self.toDraw=[]
        self.numPolygons=0
    def getModels(self):
        def getStreet():
            texture="img/streetTile1.png"
            s1=Plane([10.0,0.0,0.0],50.0,50.0,texture,50)
            #s2=Plane([0.0,0.0,0.0],10.0,5.0,texture,5)
            #s3=Plane([-5.0,0.0,0.0],10.0,5.0,texture,5)
            #s4=Plane([6.0,0.0,-2.5],5.0,10.0,texture,5)
            #s5=Plane([2.0,0.0,-5.0],5.0,10.0,texture,5)
            #s6=Plane([-4.0,0.0,1.5],5.0,10.0,texture,5)
            #s7=Plane([-7.0,0.0,5.0],5.0,10.0,texture,5)
            #s8=Plane([-4.0,0.0,-2.0],5.0,10.0,texture,5)
            #s9=Plane([8.0,0.0,-5.0],10.0,5.0,texture,5)
            #s10=Plane([4.0,0.0,-7.0],10.0,5.0,texture,5)
            #s11=Plane([-2.0,0.0,-4.0],10.0,5.0,texture,5)
            #s12=Plane([-6.0,0.0,-2.0],10.0,5.0,texture,5)
            self.toDraw.extend([s1])#,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12])
        
        getStreet()
        self.getNumPolygons()
        
        self.test=ObjLoader("models/test.obj")
        
    def getNumPolygons(self):
        for model in self.toDraw:
            self.numPolygons+=1
        print "Polygons: "+str(self.numPolygons)
    def render(self,camera):  
        for model in self.toDraw:
            model.collide(camera)
            model.render()
        
        glTranslatef(5.0,-1.25,13.0)
        self.test.render_scene()