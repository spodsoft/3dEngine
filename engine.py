from params import *
from viewManager import *
#from camera import *


class Controller():
    
    def __init__(self):
        self.running = True
        self.viewManager = ViewManager()

    def keyPressed(self,event):
        if event.type == pg.KEYDOWN:
            print(f"KeyPressed {event.key}")
        
            if event.key == pg.K_ESCAPE:
                self.running = False
            if event.key == ord('q'): 
                self.running = False
                print("Quit.")
            if event.key == ord('r'): 
                self.viewManager.camera.reset()
            if event.key == ord('a'): 
                print("A")
            if event.key == ord('s'): 
                print("S")
            if event.key == ord('d'): 
                print("D")
            if event.key == ord('f'): 
                print("F")
            if event.key == ord('z'):
                self.viewManager.object.rotate_y(-math.pi / 8)
                pass
            if event.key == pg.K_UP: 
                self.viewManager.camera.move(Direction.UP)
                pass
            if event.key == pg.K_RIGHT:
                self.viewManager.camera.move(Direction.RIGHT)
                pass
            if event.key == pg.K_DOWN:
                self.viewManager.camera.move(Direction.DOWN)
                pass
            if event.key == pg.K_LEFT:
                self.viewManager.camera.move(Direction.LEFT)
                pass
                
                
    def mouseEvent(self,event):
        pos = pg.mouse.get_pos()
        rel = pg.mouse.get_rel()
        btn = pg.mouse.get_pressed()
        
        #print ("x = {}, y = {}".format(pos[0], pos[1]))
        if event.type == pg.MOUSEMOTION:
            if btn[0] == True:
                if rel[0] < 0:
                    self.viewManager.camera.move(Direction.RIGHT,0.01)
                if rel[0] > 0:
                    self.viewManager.camera.move(Direction.LEFT,0.01)
                if rel[1] > 0:
                    self.viewManager.camera.move(Direction.UP,0.01)
                if rel[1] < 0:
                    self.viewManager.camera.move(Direction.DOWN,0.01)
            if btn[2] == True:
                if rel[0] < 0:
                    self.viewManager.camera.yaw(0.015)
                if rel[0] > 0:
                    self.viewManager.camera.yaw(-0.015)
                if rel[1] > 0:
                    self.viewManager.camera.pitch(0.015)
                if rel[1] < 0:
                    self.viewManager.camera.pitch(-0.015)
                    
        if event.type == pg.MOUSEWHEEL:
            if event.y > 0:
                self.viewManager.camera.move(Direction.INWARD)
            if event.y < 0:
                self.viewManager.camera.move(Direction.OUTWARD)        
        if event.type == pg.MOUSEBUTTONDOWN:
            #print(btn)
            if ( btn[1] == True ):
                self.viewManager.object.rotate_y(-math.pi / 8)
        if event.type == pg.MOUSEBUTTONUP:
            pass
               
    def run(self):
        while self.running:
            self.viewManager.draw()
            self.viewManager.updateFPS()
            self.viewManager.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                   self.running = False
                if event.type == pg.KEYDOWN:
                    self.keyPressed(event)
                if event.type == pg.MOUSEMOTION:
                    self.mouseEvent(event)
                if event.type == pg.MOUSEWHEEL:
                    self.mouseEvent(event)
                if event.type == pg.MOUSEBUTTONUP:
                    self.mouseEvent(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.mouseEvent(event)       
                     
if __name__ == '__main__':
    app = Controller()
    app.run()
    
    