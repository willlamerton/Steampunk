from OpenGL.GL import *
from OpenGL.GLU import *

class Wall(object):
    def __init__(self,pos,textureCoord,v1x,v1y,v1z,v2x,v2y,v2z,v3x,v3y,v3z,v4x,v4y,v4z):
        self.pos=pos
        self.textureCoord=textureCoord
        self.v1x,self.v1y,self.v1z=v1x,v1y,v1z
        self.v2x,self.v2y,self.v2z=v2x,v2y,v2z
        self.v3x,self.v3y,self.v3z=v3x,v3y,v3z
        self.v4x,self.v4y,self.v4z=v4x,v4y,v4z
        
    def render(self):
        glTranslatef(self.pos[0],self.pos[1],self.pos[2])
        glBegin(GL_QUADS)
        
        glTexCoord2f(0,self.textureCoord)
        glVertex(self.v1x,self.v1y,self.v1z) #Top Left
        
        glTexCoord2f(self.textureCoord,self.textureCoord)
        glVertex(self.v2x,self.v2y,self.v2z) #Top Right
        
        glTexCoord2f(self.textureCoord,0)
        glVertex(self.v3x,self.v3y,self.v3z) #Bottom Right
        
        glTexCoord2f(0, 0)
        glVertex(self.v4x,self.v4y,self.v4z)   #Bottom Left
        glEnd()