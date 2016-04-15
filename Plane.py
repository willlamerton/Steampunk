from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

from Texture import *

class Plane(object):
    def __init__(self,pos,width,length,texture,textureCoord):
        self.pos=pos
        self.width=width
        self.length=length
        self.textureCoord=textureCoord
        self.texture=texture
        self.logCount=0
        
    def render(self):
        Texture(self.texture)
        glTranslatef(self.pos[0],self.pos[1],self.pos[2])
        glBegin(GL_QUADS)
        
        glTexCoord2f(0,self.textureCoord)
        glVertex(self.pos[0], -1.0, self.pos[2]) #Top Left
        
        glTexCoord2f(self.textureCoord,self.textureCoord)
        glVertex(self.pos[0]-self.width, -1.0, self.pos[2]) #Top Right
        
        glTexCoord2f(self.textureCoord,0)
        glVertex(self.pos[0]-self.width, -1.0, self.pos[2]-self.length) #Bottom Right
        
        glTexCoord2f(0, 0)
        glVertex(self.pos[0], -1.0, self.pos[2]-self.length)   #Bottom Left
        glEnd()
        
    def collide(self,camera):
        if self.pos[0]+self.width>camera[0]and self.pos[0]<camera[0]:
            if self.pos[2]-self.length<camera[2]and self.pos[2]>camera[2]:
                pass
            
    def log(self,msg):
        print str(self.logCount)+": "+msg
        self.logCount+=1
        
        