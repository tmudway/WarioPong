from wario import Node

class noInput(Node):

    def __init__(self, name, params = None):
        super(noInput, self).__init__(name, params)
    
    
    def process(self):
        
        return {"Player" : [0,0]}