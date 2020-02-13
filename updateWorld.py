from wario import Node
import socket
import pickle
import pygame

UDP_IP = "127.0.0.1"
SEND_PORT = 5005

class updateWorld(Node):

    def __init__(self, name, params = None):
        super(updateWorld, self).__init__(name, params)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        
    def process(self):

        ball = self.args["Ball"]
        left = self.args["Left Paddle"]
        right = self.args["Right Paddle"]
        output = {}
        
        objects = [ball, left, right]
        
        for object in objects:
            self.global_vars["worldstate"][object["player"]].move_ip(object["movement"][0], object["movement"][1])
            output[object["player"]] = self.global_vars["worldstate"][object["player"]]

        output["score1"] = self.global_vars["worldstate"]["score"][0]
        output["score2"] = self.global_vars["worldstate"]["score"][1]

        
        self.sock.sendto(pickle.dumps(output), (UDP_IP, SEND_PORT))
        
        return