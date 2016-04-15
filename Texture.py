from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

class Texture(object):
    def __init__(self,image):
        self.image=image
        
        self.texture_surface=pygame.image.load(self.image)
        self.texture_data=pygame.image.tostring(self.texture_surface, 'RGB', True)
        self.texture_id=glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        self.w,self.h=self.texture_surface.get_rect().size
        glTexImage2D(GL_TEXTURE_2D,
                     0,
                     3,
                     self.w,
                     self.h,
                     0,
                     GL_RGB,
                     GL_UNSIGNED_BYTE,
                     self.texture_data)
    
    def delTexture(self):
        glDeleteTextures(self.texture_id)