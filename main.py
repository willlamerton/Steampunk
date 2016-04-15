from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame,sys
from pygame.locals import *

from gameobjects.matrix44 import *
from gameobjects.vector3 import *

# External Files
from Cube import *
from Plane import *
from Wall import *
from World import *

# OpenGL setup for specified display.
def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(width)/height, .1, 50.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# OpenGL setup for other settings.
def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLight(GL_LIGHT0, GL_POSITION, (1.0, 1.0, 1.0, 0.0))
    glLight(GL_LIGHT0, GL_AMBIENT, (1.0,1.0,1.0))
    glClearColor(0.4,0.3,0.3,1.0)
    
# Main Function.
def Jumping(camera):
    print "Jumping."
def run():
    pygame.init()
    global width;width=900
    global height;height=width/16*9
    global screen;screen=pygame.display.set_mode([width,height],HWSURFACE|OPENGL|DOUBLEBUF)
    pygame.display.set_caption("Steampunk")
    
    resize(width,height)
    init()
    
    clock=pygame.time.Clock()
    
    # Setup of camera matrices putting the player in a certain position.
    global camera_matrix;camera_matrix=Matrix44()
    camera_matrix.translate=(15.0,0.25,-1.0)
    
    # Setting up rotation and movement vectors to calculate movement.
    rotation_direction=Vector3()
    rotation_speed=radians(90.0)
    movement_direction=Vector3()
    movement_speed=5.0
    
    world=World()
    world.getModels()
    
    lowering=False
    jumping=False
    orgHeight=camera_matrix.translate[1]
    
    # Game loop.
    while True:
        # Set the rotation and movement vectors each loop.
        rotation_direction.set(0.0,0.0,0.0)
        movement_direction.set(0.0,movement_direction.y,0.0)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit();quit();Texture.delTexture()
            if event.type==KEYUP and event.key==K_ESCAPE:
                return
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    if jumping==False:
                        movement_direction.y=+0.7
                        jumping=True
                    #camera_matrix.translate=Jumping(camera_matrix.translate)
                    
            
        #Clear the screen.
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # Calculate time passed for frame rate.
        time_passed_seconds=clock.tick(50)/1000.
        
        # Get pressed keys for input.
        pressed=pygame.key.get_pressed()
        
        # Input handling.
        if pressed[K_a]:
            rotation_direction.y=+1.0
        if pressed[K_d]:
            rotation_direction.y=-1.0
        if pressed[K_w]:
            movement_direction.z=-1.0
        if pressed[K_s]:
            movement_direction.z=+1.0
        if pressed[K_SPACE]:
            pass
            #if newHeight<1.0:
                #newHeight+=0.1
                #camera_matrix.translate=(camera_matrix.translate[0],newHeight,camera_matrix.translate[2])
            #else:
                #newHeight-=0.1
                #camera_matrix.translate=(camera_matrix.translate[0],newHeight,camera_matrix.translate[2])
                
        if pressed[K_LSHIFT]:
            camera_matrix.move(0,0,-0.01)
        if pressed[K_LCTRL]:
            glEnable(GL_FOG)
            glFogfv(GL_FOG_COLOR, (0.4,0.3,0.3))
            glFogi(GL_FOG_MODE, GL_EXP2)
            glFogf(GL_FOG_DENSITY, 0.04)
        if pressed[K_RCTRL]:
            glDisable(GL_FOG)   
            
            
        # Transform every matrix based upon movement and time passed in order to display the scene.
        rotation=rotation_direction*rotation_speed*time_passed_seconds
        rotation_matrix=Matrix44.xyz_rotation(*rotation)
        camera_matrix*=rotation_matrix
        
        heading=Vector3(camera_matrix.forward)
        movementZ=heading*movement_direction.z*movement_speed
        camera_matrix.translate+=movementZ*time_passed_seconds
        
        # Handles Jumping.
        if jumping==True:
            movementY=Vector3(camera_matrix.up)*movement_direction.y*movement_speed
            camera_matrix.translate+=movementY*time_passed_seconds
            if camera_matrix.translate[1]>2.0:
                movement_direction.y=+0.2
                lowering=True
            #if camera_matrix.translate[1]>2.2:
                #movement_direction.y=-0.7
            if round(camera_matrix.translate[1],2)<=orgHeight and lowering==True:
                jumping=False
                lowering=False
                
        
        # Load the matrix into OpenGL to be displayed.
        glLoadMatrixd(camera_matrix.get_inverse().to_opengl())
        
        # Render World.
        world.render(camera_matrix.translate)
        
        # Update the display.
        pygame.display.flip()
        
run()