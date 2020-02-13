from wario import Node

class moveLocked(Node):

    def __init__(self, name, params = None):
        super(moveLocked, self).__init__(name, params)
    
    
    def process(self):
    
        output = self.args["Object"]
        output["movement"][0] = 0
        
        return {"Locked Object" : output}