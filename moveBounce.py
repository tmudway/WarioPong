from wario import Node
import math

objList = ["left", "right", "ball"]

class moveBounce(Node):

    def __init__(self, name, params = None):
        super(moveBounce, self).__init__(name, params)
        self.angle = -2.5
    
    def process(self):
    
        output = self.args["Object"]
        
        player = self.global_vars["worldstate"][output["player"]]
        
        movement = [self.global_vars["worldstate"]["speed"] * math.sin(self.angle),
                    self.global_vars["worldstate"]["speed"] * math.cos(self.angle)]
                    
        adjusted = player.move(movement[0], movement[1])
        
        
                # Check collision with other objects
        for obj in objList:
            if obj != output["player"]:
                objRect = self.global_vars["worldstate"][obj]
                if player.colliderect(objRect):
                    self.angle *= -1
                    movement[0] = self.global_vars["worldstate"]["speed"] * math.sin(self.angle)
                    adjusted = player.move(movement[0], movement[1])
        
        # Check collision with top/bottom
        if adjusted[1] < 0 or adjusted[1] > 600 - player[3]:
            self.angle *= -1
            self.angle -= 3.14159265358
            
        if adjusted[0] < 0 or adjusted[0] > 800 - player[2]:
            self.angle *= -1
        

                    
        output["movement"] = movement
        
        return {"Bounced Object" : output}