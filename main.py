import pygame
from settings import *
from sys import exit
from tetramino import *

def main():

    pygame.init()

    screen = pygame.display.set_mode(screen_size)

    FPS = 30
    clock = pygame.time.Clock()


    current_piece = Tetramino(3,-4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x-=1
                if event.key == pygame.K_RIGHT:
                    current_piece.x+=1
                if event.key == pygame.K_DOWN:
                    current_piece.y+=1
                if event.key == pygame.K_r:
                    current_piece = Tetramino(3,0)
                if event.key == pygame.K_s:
                    current_piece.set(game_stack)

        if current_piece.move_timer < 60:
            current_piece.move_timer+=1
        else:
            current_piece.move_timer=0
            current_piece.y+=1

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
    current_piece.draw(screen)

if __name__ == "__main__":
    main()

