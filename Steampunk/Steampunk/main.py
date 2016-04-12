from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

from gameobjects.matrix44 import *
from gameobjects.vector3 import *

# External Files
from Cube import *
from Plane import *

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
    glClearColor(0.0,0.6,1.0,0.5)
        
# Main Function.
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
    camera_matrix=Matrix44()
    camera_matrix.translate=(10.0,0.0,10.0)
    
    # Setting up rotation and movement vectors to calculate movement.
    rotation_direction=Vector3()
    rotation_speed=radians(90.0)
    movement_direction=Vector3()
    movement_speed=5.0
    
    plane1=Plane([10.0,0.0,0.0],20.0,20.0,[0.0,0.6,0.0])
    
    # Game loop.
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit();quit()
            if event.type==KEYUP and event.key==K_ESCAPE:
                return
                
        
        #Clear the screen.
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # Calculate time passed for frame rate.
        time_passed_seconds=clock.tick()/1000.
        
        # Get pressed keys for input.
        pressed=pygame.key.get_pressed()
        
        # Set the rotation and movement vectors each loop.
        rotation_direction.set(0.0,0.0,0.0)
        movement_direction.set(0.0,0.0,0.0)
        
        # Input handling.
        if pressed[K_a]:
            rotation_direction.y=+1.0
        if pressed[K_d]:
            rotation_direction.y=-1.0
        if pressed[K_w]:
            movement_direction.z=-1.0
        if pressed[K_s]:
            movement_direction.z=+1.0
        
        
        # Transform every matrix based upon movement and time passed in order to display the scene.
        rotation=rotation_direction*rotation_speed*time_passed_seconds
        rotation_matrix=Matrix44.xyz_rotation(*rotation)
        camera_matrix*=rotation_matrix
        
        heading=Vector3(camera_matrix.forward)
        movement=heading*movement_direction.z*movement_speed
        camera_matrix.translate+=movement*time_passed_seconds
        
        # Load the matrix into OpenGL to be displayed.
        glLoadMatrixd(camera_matrix.get_inverse().to_opengl())
        
        # Draw the cube.
        plane1.render()
        
        # Update the display.
        pygame.display.flip()
        
run()