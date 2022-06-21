from tabnanny import check
import pygame
from settings import *
from sys import exit

from tetramino import *

def main():

    pygame.init()

    screen = pygame.display.set_mode(screen_size)

    FPS = 60
    clock = pygame.time.Clock()


    current_piece = O(3,-4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(current_piece,"L"):
                    current_piece.x-=1
                if event.key == pygame.K_RIGHT and not check_collision(current_piece,"R"):
                    current_piece.x+=1
                if event.key == pygame.K_DOWN and not check_collision(current_piece,"D"):
                    current_piece.y+=1
                if event.key == pygame.K_r:
                    current_piece = O(0,0)

        current_piece.update()
        if check_collision(current_piece,"D"):
            for piece_y in range(4):
                for piece_x in range(4):
                    if current_piece.shapes[0][piece_y][piece_x]:
                        game_stack[current_piece.y+piece_y][current_piece.x+piece_x]=True
                        color_stack[current_piece.y+piece_y][current_piece.x+piece_x]=current_piece.color
            current_piece = O(3,-4)
            current_piece.color+=1

        draw_field(screen, current_piece)

        pygame.display.update()
        clock.tick(FPS)

    

def draw_field(screen, current_piece):
    # Copy the current stack into a temp stack
    draw_stack = game_stack

    # Draw stack
    for stack_y in range(20):
        for stack_x in range(10):
            cell_surf = pygame.surface.Surface((tile_size-border, tile_size-border))
            cell_rect = cell_surf.get_rect(topleft = (stack_x*tile_size,stack_y*tile_size))
            cell_surf.fill(colors[color_stack[stack_y][stack_x]])
            screen.blit(cell_surf,cell_rect)

    # Draw current piece
    draw_piece(current_piece,screen)


def draw_piece(piece,screen):
    for piece_y in range(4):
        for piece_x in range(4):
            if piece.shapes[0][piece_y][piece_x]:
                piece_surf = pygame.surface.Surface((tile_size-border,tile_size-border))
                piece_rect = piece_surf.get_rect(topleft = ((piece.x+piece_x)*tile_size, (piece.y+piece_y)*tile_size))
                piece_surf.fill(colors[piece.color])
                screen.blit(piece_surf,piece_rect)

    
def check_collision(piece,dir):
    # LEFT
    for piece_y in range(4):
        for piece_x in range(4):
            if piece.shapes[0][piece_y][piece_x]:
                if piece.x+piece_x-1 == -1 and dir == "L":
                    return True
                if piece.x+piece_x+1 == 10 and dir == "R":
                    return True
                if piece.y+piece_y+1==20 and dir == "D":
                    return True

if __name__ == "__main__":
    main()

