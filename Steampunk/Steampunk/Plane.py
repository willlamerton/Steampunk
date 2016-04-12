from OpenGL.GL import *
from OpenGL.GLU import *

class Plane(object):
    def __init__(self,pos,width,length,colour):
        self.pos=pos
        self.width=width
        self.length=length
        self.colour=colour
        
    def render(self):
        glTranslatef(self.pos[0],self.pos[1],self.pos[2])
        glBegin(GL_QUADS)
        glColor3fv(self.colour)
        glVertex(self.pos[0], -1.0, self.pos[2]) #Top Left
        glVertex(self.pos[0]-self.width, -1.0, self.pos[2]) #Top Right
        glVertex(self.pos[0]-self.width, -1.0, self.pos[2]-self.length) #Bottom Right
        glVertex(self.pos[0], -1.0, self.pos[2]-self.length)   #Bottom Left
        glEnd()