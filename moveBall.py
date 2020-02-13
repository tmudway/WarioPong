from wario import Node

class moveBall(Node):

    def __init__(self, name, params = None):
        super(moveBall, self).__init__(name, params)
    
    
    def process(self):
    
        if "Player" in self.args.keys():
            input = self.args["Player"]
        else:
            input = [0,0]
        paddle = self.global_vars["worldstate"]["ball"]
        movement = [input[0] * self.global_vars["worldstate"]["speed"], input[1] * self.global_vars["worldstate"]["speed"]]
        
        adjusted = [paddle[i] + movement[i] for i in range(2)]
        
        # Ball collisions. Dont do top/bottom/paddle as we do that
        # in the bounce node
        
        if adjusted[0] < 0:
            movement[0] = 0
            movement[1] = 0
            self.global_vars["worldstate"]["ball"][0] = 395
            self.global_vars["worldstate"]["ball"][1] = 295
            self.global_vars["worldstate"]["score"][1] += 1
        elif adjusted[0] > 790:
            movement[0] = 0
            movement[1] = 0
            self.global_vars["worldstate"]["ball"][0] = 395
            self.global_vars["worldstate"]["ball"][1] = 295
            self.global_vars["worldstate"]["score"][0] += 1
            
        output = {
                  "player" : "ball",
                  "movement" : movement
                 }
        
        return {"Ball Movement" : output}