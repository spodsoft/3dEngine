from params import *
from matrix_utils import *
import numpy as np
#import math

class Camera():
    
    def __init__(self):
        self.reset()

    def reset(self):
        self.x              = 0
        self.y              = 0
        self.z              = -10
        self.anglePitch     = 0
        self.angleYaw       = 0
        self.angleRoll      = 0
        
        self.moving_speed   = 0.3
        self.rotation_speed = 0.015
                
    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()

    def yaw(self, angle):
        self.angleYaw   += angle

    def pitch(self, angle):
        self.anglePitch += angle    
        
    def resetMatrix(self):
        self.forward    = np.array([0, 0, 1, 1])
        self.up         = np.array([0, 1, 0, 1])
        self.right      = np.array([1, 0, 0, 1])      
        
    def translate_matrix(self):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-self.x, -self.y, -self.z, 1]
        ])  

    def rotate_matrix(self):
        rotate = rotate_x(self.anglePitch) @ rotate_y(self.angleYaw)  # this concatenation gives right visual
        return identity @ rotate
        
    def move(self,direction, speed = 0.3):
        if direction== Direction.LEFT:
            self.x -= speed
        if direction== Direction.RIGHT:
            self.x += speed
            
        if direction== Direction.DOWN:
            self.y -= speed
        if direction== Direction.UP:
            self.y += speed
            
        if direction== Direction.OUTWARD:
            self.z += speed
        if direction== Direction.INWARD:
            self.z -= speed


