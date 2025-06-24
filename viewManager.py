from params import *
import pygame as pg
import os
from vertex import *

from camera import *
#from screenProjection import *
from object3d import *

class ViewManager():
    
    def __init__(self):
        self.camera = Camera()
        
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 18)
        self.delta_time = 1
        
        pg.display.set_caption("RT")

        self.create_objects()
        self.axes = Axes()

    def create_objects(self):
        #self.object = self.get_object_from_file('resources/t_34_obj.obj')
        self.object = Cube()
        
    def get_object_from_file(self, filename):
        #file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_dir = os.path.dirname(__file__)

        file_name = os.path.join(file_dir, filename)
        vertex, faces = [], []

        with open(file_name) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    # split on space
                    faces_ = line.split()[1:]

                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
                    
        object = Object3d()
        object.setVertices(vertex)
        object.setFaces(faces)
        
        return object
        

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))

        self.object.draw(self.screen, self.camera)
        self.axes.draw(self.screen,self.camera)
        
        pg.display.flip()
        
    def update(self):
        pg.display.flip()        

    def updateFPS(self):
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.1f}' )
        self.clock.tick(FPS)
        
        #self.delta_time += self.clock.tick(30)
        # don't refresh the OSD more than once per sec.
        #if self.delta_time > 1000:
        #    self.delta_time = 0
        #   self.clockText = self.font.render(f'fps: {self.clock.get_fps():.1f}', True, (255, 255, 0))
