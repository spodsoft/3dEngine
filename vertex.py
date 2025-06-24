import pygame as pg
import pygame.math as pgmath


class Vertex():
    
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        
        self.screen_coords = pgmath.Vector2(x,y) 
        
        
    