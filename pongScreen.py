import pygame
import sys
import socket
import json
import pickle
from wario.PipelineThread import PipelineThread
from PyQt5 import QtWidgets
    
UDP_IP = "127.0.0.1"
SEND_PORT = 5006
GET_PORT = 5005

# Setup Pygame window
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255   

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
p1Paddle = pygame.image.load("paddle.png")
p2Paddle = pygame.image.load("paddle.png")

ft = pygame.font.SysFont("monospace", 45)

screen.fill(black)
pygame.draw.line(screen, white, (400, 0), (400, 600), 3)
        
# Start WARIO pipeline        
PipelineThread("./pong.json").start()
pygame.time.wait(100)

# Setup sockets        
        
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, GET_PORT))
sock.setblocking(0)

inputState = {  
                "p1State" : [0,0],
                "p2State" : [0,0]
            }
            
sock.sendto(json.dumps(inputState).encode('utf-8'), (UDP_IP, SEND_PORT))



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sock.sendto(json.dumps(-1).encode('utf-8'), (UDP_IP, SEND_PORT))
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                inputState["p1State"][1] = -1
            if event.key == pygame.K_s:
                inputState["p1State"][1] = 1
            if event.key == pygame.K_a:
                inputState["p1State"][0] = -1
            if event.key == pygame.K_d:
                inputState["p1State"][0] = 1
                
            if event.key == pygame.K_UP:
                inputState["p2State"][1] = -1
            if event.key == pygame.K_DOWN:
                inputState["p2State"][1] = 1
            if event.key == pygame.K_LEFT:
                inputState["p2State"][0] = -1
            if event.key == pygame.K_RIGHT:
                inputState["p2State"][0] = 1
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                if inputState["p1State"][1] < 0:
                    inputState["p1State"][1] = 0
            if event.key == pygame.K_s:
                if inputState["p1State"][1] > 0:
                    inputState["p1State"][1] = 0  
            if event.key == pygame.K_a:
                if inputState["p1State"][0] < 0:
                    inputState["p1State"][0] = 0
            if event.key == pygame.K_d:
                if inputState["p1State"][0] > 0:
                    inputState["p1State"][0] = 0 
                    
            if event.key == pygame.K_UP:
                if inputState["p2State"][1] < 0:
                    inputState["p2State"][1] = 0
            if event.key == pygame.K_DOWN:
                if inputState["p2State"][1] > 0:
                    inputState["p2State"][1] = 0
            if event.key == pygame.K_LEFT:
                if inputState["p2State"][0] < 0:
                    inputState["p2State"][0] = 0
            if event.key == pygame.K_RIGHT:
                if inputState["p2State"][0] > 0:
                    inputState["p2State"][0] = 0
    try:
       
        data, addr = sock.recvfrom(1024)
        state = pickle.loads(data)
        sock.sendto(json.dumps(inputState).encode('utf-8'), (UDP_IP, SEND_PORT))
        
        screen.fill(black)
        pygame.draw.line(screen, white, (400, 0), (400, 600), 3)
        
        screen.blit(ball, state["ball"])
        screen.blit(p1Paddle, state["left"])
        screen.blit(p2Paddle, state["right"])
        
        score1 = ft.render("{0}".format(state["score1"]), True, white)
        score2 = ft.render("{0}".format(state["score2"]), True, white)
        screen.blit(score1, (310, 10))
        screen.blit(score2, (470, 10))
        

    except:
        pass
        


    pygame.display.flip()
    pygame.time.wait(33)