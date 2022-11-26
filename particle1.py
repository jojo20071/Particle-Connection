import sys
import pygame
from pygame.locals import *
pygame.init()
import random

vel = []
pos = []
amount = 100
start = True
sens = 100
speed=10
speed2 = 10


width, height = 1000,1000
screen = pygame.display.set_mode((width, height))

def left():
    pos[i][0] = 0
    pos[i][1] = random.randint(0,1000)
def right():
    pos[i][0] = 1000
    pos[i][1] = random.randint(0,1000)
def up():
    pos[i][0] = random.randint(0,1000)
    pos[i][1] = 0
def down():
    pos[i][0] = random.randint(0,1000)
    pos[i][1] = 1000

def r_vel():
    a = random.randint(-speed,speed)
    if a != 0:
        return a
    else:
        return r_vel()
                
   

 
# Game loop.
while True:
    
    m_pos = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Update.
    for i in range(amount):
        if start:
            pos.append([random.randint(1,1000),random.randint(1,1000)])
            vel.append([r_vel(),r_vel()])
            if i == 99:
                pos.append(m_pos)	
        else:
            pos[i][0]+=(vel[i][0])/speed2
            pos[i][1]+=(vel[i][1])/speed2
            for r in range(amount-i+1):
                if ((pos[i][0] - pos[i+r][0] < 0 and pos[i][0] - pos[i+r][0] > -sens) or (pos[i][0] - pos[i+r][0] > 0 and pos[i][0] - pos[i+r][0] < sens)) and ((pos[i][1] - pos[i+r][1] < 0 and pos[i][1] - pos[i+r][1] > -sens) or (pos[i][1] - pos[i+r][1] > 0 and pos[i][1] - pos[i+r][1] < sens)):
                    if pos[i][0] - pos[i+r][0] < 0:
                        x = (pos[i][0] - pos[i+r][0]) * -1
                    else:
                        x = pos[i][0] - pos[i+r][0]
                    if pos[i][1] - pos[i+r][1] < 0:
                        y = (pos[i][1] - pos[i+r][1]) * -1
                    else:
                        y = pos[i][1] - pos[i+r][1]
                    tra = (200-(y + x))/2
                    #print(tra)
                    pygame.draw.line(screen, (int(2.55*tra), int(2.55*tra), int(2.55*tra)), (pos[i][0], pos[i][1]), (pos[i+r][0], pos[i+r][1]), 2)
            pygame.draw.circle(screen, (255, 255, 255), (pos[i][0], pos[i][1]), 3)
            if pos[i][0] > 1000 or pos[i][0] < 0:
                random.choice([left,right])()
            if pos[i][1] < 0 or pos[i][1] > 1000:
                random.choice([up,down])()
            if i == 99:
                pos[100] = m_pos      
                pygame.draw.circle(screen, (255, 255, 255), (pos[100]), 3)   
            
    # Draw.
    start = False
    pygame.display.flip()