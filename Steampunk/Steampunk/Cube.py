# Draw a cube.
from OpenGL.GL import *
from OpenGL.GLU import *

class Cube(object):
    def __init__(self,pos,colour):
        self.pos=pos
        self.colour=colour
        
        self.verticies=self.verticies=(
            (1,-1,-1),#back bottom right
            (1,1,-1), #back top right
            (-1,1,-1), #back top left
            (-1,-1,-1), #back bottom left
            (1,-1,1), #front bottom right
            (1,1,1), #front top right
            (-1,-1,1), #front top left
            (-1,1,1) #front bottom right
        )
        self.edges=(
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7)
        )
        self.surfaces = (
            (0, 1, 2, 3),  # front
            (3, 2, 7, 6),  # back
            (6, 7, 5, 4),  # right
            (4, 5, 1, 0),  # left
            (1, 5, 7, 2),  # top
            (4, 0, 3, 6)   # bottom
        )
    
    def render(self):
        glTranslatef(self.pos[0],self.pos[1],self.pos[2])
        
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for vertex in surface:
                glColor3fv(self.colour)
                glVertex3fv(self.verticies[vertex])
        glEnd()
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3fv((0.0,0.0,0.0))
                glVertex3fv(self.verticies[vertex])
        glEnd()
        