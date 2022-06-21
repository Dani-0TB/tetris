colors = [(0,0,0),
    (235, 64, 52),
    (235, 201, 52),
    (24, 181, 24),
    (113, 206, 235), 
    (223, 113, 235),
    (237, 137, 43)]

class Tetramino:
    def __init__(self):
        self.move_timer = 0
        self.shape = [
            [False,False,False,False],
            [False,False,False,False],
            [False,False,False,False],
            [False,False,False,False]]

    def update(self):
        if self.move_timer < 60:
            self.move_timer += 1
        else:
            self.move_timer=0
            self.y+=1


class O(Tetramino):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.color = 2
        self.shapes = [[
            [False,False,False,False],
            [False,True,True,False],
            [False,True,True,False],
            [False,False,False,False]]]
