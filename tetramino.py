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
    [[1,2,5,6]],    #O 0
    [[1,5,9,10]],   #L 1
    [[1,5,8,9]],    #J 2
    [[1,5,6,10]],   #N 3
    [[0,1,5,6]],    #Z 4
    [[1,4,5,6]],    #T 5
    [[2,6,10,14]]   #I 6
]

class Tetramino:
    def __init__(self, x, y):
        self.move_timer = 0
        self.x=x
        self.y=y
        self.shape=randint(0,len(shapes)-1)
        self.rotation=0
        self.shapes=shapes[self.shape][self.rotation]
        self.color=self.shape+1
    
    def draw(self,screen):
        counter = 0
        for cell_y in range(4):
            for cell_x in range(4):
                if counter in self.shapes:
                    piece_surf = pygame.surface.Surface((tile_size-border,tile_size-border))
                    piece_rect = piece_surf.get_rect(topleft = ((self.x+cell_x)*tile_size, (self.y+cell_y)*tile_size))
                    piece_surf.fill(colors[self.color])
                    screen.blit(piece_surf,piece_rect)
                counter += 1

    def set(self,stack):
        counter = 0
        for cell_y in range(4):
            for cell_x in range(4):
                if counter in self.shapes:
                    game_stack[self.y+cell_y][self.x+cell_x]=True
                    color_stack[self.y+cell_y][self.x+cell_x]=self.color
                counter += 1