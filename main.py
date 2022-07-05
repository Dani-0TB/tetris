import pygame
from settings import *
from sys import exit
from tetramino import *
from os import system

def main():

    pygame.init()

    screen = pygame.display.set_mode(screen_size)

    FPS = 60
    clock = pygame.time.Clock()

    

    current_piece = Tetramino(3,1)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # Player Controller
                if event.key == pygame.K_LEFT:
                    if not current_piece.collide(3):
                        current_piece.x-=1
                if event.key == pygame.K_RIGHT:
                    if not current_piece.collide(1):
                        current_piece.x+=1
                if event.key == pygame.K_UP:
                    drop_piece(current_piece)
                    current_piece.move_timer = 0
                if event.key == pygame.K_DOWN:
                    if current_piece.collide(2):
                        pass
                    else:
                        current_piece.y+=1
                if event.key == pygame.K_z:
                    current_piece.rotate(1)
                if event.key == pygame.K_x:
                    current_piece.rotate(2)
                
                # Game settings controls
                if event.key == pygame.K_r:
                    current_piece.x = 3
                    current_piece.y = 1
                
                

                if event.key == pygame.K_c:
                    clear_stack()
        
        # Move timer
        if current_piece.move_timer < time:
            current_piece.move_timer+=1
        else:
            current_piece.move_timer=0
            if current_piece.collide(2):
                current_piece.set()
            else:
                current_piece.y+=1

        ## Reset board if topped out.
        for i in range(10):
            if game_stack[4][i]:
                clear_stack()
                current_piece.x = 3
                current_piece.y = 1
                current_piece.shape = randint(0,7)
        
        check_lines()
        
        draw_field(screen, current_piece)

        pygame.display.update()
        clock.tick(FPS)



def draw_field(screen, current_piece):
    # Copy the current stack into a temp stack
    draw_stack = game_stack

    # Draw stack
    for stack_y in range(25):
        for stack_x in range(10):
                cell_surf = pygame.surface.Surface((tile_size-border, tile_size-border))
                cell_rect = cell_surf.get_rect(topleft = (stack_x*tile_size,(stack_y-5)*tile_size))
                cell_surf.fill(colors[color_stack[stack_y][stack_x]])
                screen.blit(cell_surf,cell_rect)

    # Draw current piece
    current_piece.draw(screen)


def clear_stack():
    for y in range(25):
        for x in range(10):
            game_stack[y][x] = False
            color_stack[y][x] = 0

            
def check_lines():
    lines_to_clear = 0
    index = 0
    indices = []
    clear = True
    for row in game_stack:
        for cell in row:
            if not cell:
                clear = False
                continue
        if clear:
            lines_to_clear+=1
            indices.append(index)    
        index +=1
        clear=True

    if lines_to_clear > 0:
        clear_lines(indices)

def clear_lines(indices):
    for item in indices:
        rows = range(1,item+1)
        for row in rows[::-1]:
            for cell in range(10):
                game_stack[row][cell] = game_stack[row-1][cell]
                color_stack[row][cell] = color_stack[row-1][cell]


        
            
    
def drop_piece(piece):
    for i in range(20):
        if not piece.collide(2):
            piece.y+=1


if __name__ == "__main__":
    main()

