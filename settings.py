game_stack = []

# Inicializar el Stack
for i in range(25):
    row = []
    for j in range(10):
        row.append(False)
    game_stack.append(row)

# Inicializar array de colores
color_stack=[]

for i in range(25):
    row = []
    for j in range(10):
        row.append(0)
    color_stack.append(row)

tile_size = 32
screen_size = width, height = tile_size*10, tile_size*20
border = 4
lines_cleared = 0
time = 30
