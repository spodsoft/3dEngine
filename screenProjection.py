import math
import numpy as np
from params import *

# https://xdpixel.com/decoding-a-projection-matrix/

class ScreenProjection:
    
    
    def __init__(self):    
        NEAR    = NEAR_PLANE
        FAR     = FAR_PLANE
        RIGHT   = math.tan(HORIZONTAL_FOV / 2)
        LEFT    = -RIGHT
        TOP     = math.tan(VERTICAL_FOV / 2)
        BOTTOM  = -TOP

        m00 = 2  / (RIGHT - LEFT)               # Controls how much the image is stretched or squashed horizontally. 
        m11 = 2 * NEAR / (TOP - BOTTOM)         # Controls how much the image is stretched or squashed vertically.
        m22 = (FAR + NEAR) / (FAR - NEAR)       # Controls whether or not an object clipped based on its depth.  
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        
        m23 = 1                                 # 1= Left handed coords, -1 =right handed, 0 = not perspective
        
        
        # Replacement mapping
        m00 = 1.0 / math.tan(HORIZONTAL_FOV / 2)
        m11 = 1.0 / math.tan(HORIZONTAL_FOV / 2)
        m22 = FAR / (FAR-NEAR)
        m32 = - FAR * NEAR / (FAR-NEAR)
        
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, m23],
            [0, 0, m32, 0]
        ])
        
        HW, HH = HALF_WIDTH, HALF_HEIGHT
        self.screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])
        
