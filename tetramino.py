import pygame
from random import randint
from settings import *

colors = [(0,0,0),  #BLACK
    (232, 183, 21), #YELLOW
    (245, 71, 32),  #ORANGE
    (11, 3, 161),   #BLUE
    (42, 179, 27),  #GREEN
    (227, 16, 16),  #RED
    (57, 14, 138),  #PURPLE
    (99, 182, 230)] #SKY

shapes = [
    [[1,2,5,6]],                                    #O 0
    [[2,4,5,6],[0,1,5,9],[4,5,6,8],[1,5,9,10]],     #L 1
    [[0,4,5,6],[1,5,8,9],[4,5,6,10],[1,2,5,9]],     #J 2
    [[1,2,4,5],[0,4,5,9],[5,6,8,9],[1,5,6,10]],     #N 3
    [[0,1,5,6],[1,4,5,8],[4,5,9,10],[2,5,6,9]],     #Z 4
    [[1,4,5,6],[1,4,5,9],[4,5,6,9],[1,5,6,9]],      #T 5
    [[8,9,10,11],[1,5,9,13],[4,5,6,7],[2,6,10,14]]  #I 6
]

class Tetramino:
    def __init__(self, x, y):
        self.move_timer = 0
        self.x=x
        self.y=y
        self.shape=randint(0,len(shapes)-1)
        self.rotation=0
        self.shapem=shapes[self.shape][self.rotation]
        self.color=self.shape+1
    
    def draw(self,screen):
        counter = 0
        for cell_y in range(4):
            for cell_x in range(4):
                if counter in self.shapem:
                    piece_surf = pygame.surface.Surface((tile_size-border,tile_size-border))
                    piece_rect = piece_surf.get_rect(topleft = ((self.x+cell_x)*tile_size, (self.y+cell_y-5)*tile_size))
                    piece_surf.fill(colors[self.color])
                    screen.blit(piece_surf,piece_rect)
                counter += 1

    def set(self):
        counter = 0
        for cell_y in range(4):
            for cell_x in range(4):
                if counter in self.shapem:
                    game_stack[self.y+cell_y][self.x+cell_x]=True
                    color_stack[self.y+cell_y][self.x+cell_x]=self.color
                counter += 1
        self.x = 3
        self.y = 1
        self.shape = randint(0,len(shapes)-1)
        self.rotation = 0
        self.shapem=shapes[self.shape][self.rotation]
        self.color=self.shape+1
    
    def collide(self,dir,r=False):
        counter = 0
        for cell_y in range(4):
            for cell_x in range(4):
                if counter in self.shapem:
                    if dir == 2: #DOWN
                        if (self.y+cell_y+1) >= 25:
                            return True
                        if game_stack[self.y+cell_y+1][cell_x+self.x]:
                            return True
                    elif dir == 3:
                        if self.x+cell_x - 1 <= -1:
                            return True
                        if not r:
                            if game_stack[self.y+cell_y][cell_x+self.x-1]:
                                return True
                    elif dir == 1:
                        if self.x+cell_x + 1 >= 10:
                            return True
                        if not r:
                            if game_stack[self.y+cell_y][cell_x+self.x+1]:
                                return True
                        
                counter+=1
    
    def rotate(self,dir):
        if not self.collide(3) and not self.collide(1):
            if dir == 1:
                if self.rotation == len(shapes[self.shape])-1:
                    self.rotation = 0
                else:
                    self.rotation += 1
            if dir == 2:
                if self.rotation == 0:
                    self.rotation = len(shapes[self.shape])-1
                else:
                    self.rotation -= 1
            
            self.shapem = shapes[self.shape][self.rotation]