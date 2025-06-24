import numpy as np
import pygame as pg
from screenProjection import *
from matrix_utils import *

class Object3d():
    
    def __init__(self):
        self.vertices = np.array([])
        self.edges    = list()
        self.faces    = list()
        self.projection = ScreenProjection()
        
        
    def setVertices(self, vertices: list[list[float]] ):
        self.vertices = vertices
        
    def setFaces(self, faces: list[list[int]]):
        self.faces = faces
        self.buildEdges()
               
    def rotate(self,angle):
        self.vertices = self.vertices @ rotate_y(angle)
        
    def buildEdges(self):
        self.edges  = list()
        
        for face in self.faces:
            
            firstEdge = True
            for e in face:
                if ( firstEdge ):
                    edge1 = e
                    firstEdge = False
                else:
                    edge2 = e
                    self.edges.append([edge1,edge2])
       
        
    def draw(self, display, camera):

        colour  = pg.Color('white')
        colour1 = pg.Color('orange')
        colour2 = pg.Color('green')
        flip    = False
        screen_vertices = self.vertices @ camera.camera_matrix()
        screen_vertices = screen_vertices @ self.projection.projection_matrix 
        screen_vertices /= screen_vertices[:, -1].reshape(-1, 1)
        screen_vertices = screen_vertices @ self.projection.screen_matrix

        depths = screen_vertices[:,2:3]

        screen_vertices = screen_vertices[:,:2]

        for edge in self.edges:
            depth0 = depths[edge[0]]
            depth1 = depths[edge[1]]
            v1 = screen_vertices[edge[0]]
            v2 = screen_vertices[edge[1]]

            if ( depths[edge[0]] < 0 ) | (depths[edge[1]] < 0) | ( depths[edge[0]] > 1 ) | (depths[edge[1]] > 1) :
                pass
            else:
                if flip:
                    colour = colour1
                else:
                    colour = colour2
                
                flip = not flip
                pg.draw.line(display,colour,v1,v2)

        self.rotate(-math.pi / 800)
        
class Cube(Object3d):
    
    def __init__(self):
        super().__init__()  
        
        self.vertices = np.array([
            (-2, -2, -2, 1),
            (2, -2, -2, 1),
            (2, 2, -2, 1),
            (-2, 2, -2, 1),
            (-2, -2, 2, 1),
            (2, -2, 2, 1),
            (2, 2, 2, 1),
            (-2, 2, 2, 1)  ])
        self.edges = list([
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 4],
            [0, 4],
            [1, 5],
            [2, 6],
            [3, 7] ])

        self.faces = list([
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [1, 2, 6, 5],
            [2, 3, 7, 6],
            [3, 0, 4, 7] ])
        
        
class Axes(Object3d):
    def __init__(self):
        super().__init__()
        self.vertices = np.array([(0, 0, 0, 1), (10, 0, 0, 1), (0, 10, 0, 1), (0, 0, 10, 1)])
        self.edges = np.array([(0, 1), (0, 2), (0, 3)])
        self.faces = np.array([])
        
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
#
        self.draw_vertices = False
        self.label = 'XYZ'
        
    def draw(self, display, camera):
#
        screen_vertices = self.vertices @ camera.camera_matrix()
        screen_vertices = screen_vertices @ self.projection.projection_matrix 
        screen_vertices /= screen_vertices[:, -1].reshape(-1, 1)
        screen_vertices = screen_vertices @ self.projection.screen_matrix

        depths = screen_vertices[:,2:3]

        screen_vertices = screen_vertices[:,:2]

        for index in range(0,len(self.colors)):
            theEdge = self.edges[index]
            
            depth0 = depths[theEdge[0]]
            depth1 = depths[theEdge[1]]

            if ( depths[theEdge[0]] < 0 ) | (depths[theEdge[1]] < 0) | ( depths[theEdge[0]] > 1 ) | (depths[theEdge[1]] > 1) :
                pass
            else:
                v1 = screen_vertices[theEdge[0]]
                v2 = screen_vertices[theEdge[1]]
            
                colour = self.colors[index]
           
                pg.draw.line(display,colour,v1,v2)


