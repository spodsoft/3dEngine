import math
from enum import Enum
    
RES = WIDTH, HEIGHT = 1000, 1000
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2

HORIZONTAL_FOV  = math.pi / 3
VERTICAL_FOV    = math.pi / 3

NEAR_PLANE = 0.01
FAR_PLANE = 100

FPS = 60

class Direction(Enum):
    LEFT      = 0
    RIGHT     = 1
    UP        = 2
    DOWN      = 3
    INWARD    = 4
    OUTWARD   = 5
