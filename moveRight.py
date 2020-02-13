from wario import Node

class moveRight(Node):

    def __init__(self, name, params = None):
        super(moveRight, self).__init__(name, params)
    
    
    def process(self):
        if "Player" in self.args.keys():
            input = self.args["Player"]
        else:
            input = [0,0]
            
        paddle = self.global_vars["worldstate"]["right"]
        movement = [input[0] * self.global_vars["worldstate"]["speed"], input[1] * self.global_vars["worldstate"]["speed"]]
        
        adjusted = [paddle[i] + movement[i] for i in range(2)]
        
        # Right paddle collisions
        if adjusted[0] < 400:
            movement[0] = 400 - paddle[0]
        elif adjusted[0] > 790:
            movement[0] = 790 - paddle[0]
        
        if adjusted[1] < 0:
            movement[1] = -1 * paddle[1]
        elif adjusted[1] > 550:
            movement[1] = 550 - paddle[1] 
            
        output = {
                  "player" : "right",
                  "movement" : movement
                 }
        
        return {"Paddle Movement" : output}