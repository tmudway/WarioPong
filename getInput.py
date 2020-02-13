from wario import Node
import socket
import json
import pygame

UDP_IP = "127.0.0.1"
GET_PORT = 5006



class getInput(Node):

    def __init__(self, name, params = None):
        super(getInput, self).__init__(name, params)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, GET_PORT))
        self.done = False
        
        
    def process(self):
        
        if "worldstate" not in self.global_vars.keys():
            self.global_vars["worldstate"] = {
                                        "ball" : pygame.Rect(395, 295, 10, 10),
                                        "left" : pygame.Rect(0, 295, 10, 50),
                                        "right" : pygame.Rect(790, 295, 10, 50),
                                        "score" : [0,0],
                                        "ballAngle" : -2.5,
                                        "speed" : 10
                                     }
    
        data, addr = self.sock.recvfrom(1024)
        state = json.loads(data.decode('utf-8'))
        
        if state == -1:
            self.done = True
            state = {"p1State" : [0,0], "p2State" : [0,0]}
            
               
        return {"WASD" : state["p1State"], "Arrows" : state["p2State"]}