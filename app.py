import os
from time import sleep


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for x in range(width)] for y in range(height)]
    
    def __normalize_coords(self, x, y):
        """ Summer's code for infinite gridding """
        if x >= self.width:
            x = x - self.width
            y = self.height - y
        elif x < 0:
            x = x + self.width
            y = self.height - y
        
        if y >= self.height:
            y = y - self.height
        elif y < 0:
            y = y + self.height
        
        return (x, y)

    def _get(self, x, y):
        x, y = self.__normalize_coords(x, y)
        return self.grid[y][x]
    
    def _set(self, x, y, val):
        x, y = self.__normalize_coords(x, y)
        self.grid[y][x] = val

    def _crowd_count(self, x, y):
        count = 0
        coords = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        for coord in coords:
            if 0 < self._get(x + coord[0], y + coord[1]):
                count += 1
        
        return count

    def next(self):
        """ Transition grid with conway game of life rules """
        to_change = []
        for y in range(self.height):
            for x in range(self.width):
                crowd = self._crowd_count(x, y)
                if self._get(x, y) > 0:
                    # Currently Alive
                    if crowd < 2 or crowd > 3:
                        to_change.append((x, y, 0))
                else:
                    # Currently Dead
                    if crowd == 3:
                        to_change.append((x, y, 1))
        
        for change in to_change:
            self._set(change[0], change[1], change[2])

                
    def insert_seed(self, x0, y0, character):
        height=len(character)
        width=len(character[0])
        for y in xrange(height):
            for x in xrange(width):
                self._set(x+x0, y+y0, character[y][x])

    def out(self):
        frame = ""
        num_div=" "
        for row in self.grid:
            vals=""
            for num in row:
                vals+=num_div
                if num == 1:
                    vals += "@"
                else:
                    vals += " "
            vals+=num_div + "|"
            frame += "{}\n".format(vals)

        frame += "_" * 2 * self.width + "_|"
        print(frame)


beehive=[[0,1,1,0],[1,0,0,1],[0,1,1,0]]
block=[[1,1],[1,1]]
loaf=[[0,1,1,0],[1,0,0,1],[0,1,0,1],[0,0,1,0]]
boat=[[1,1,0],[1,0,1],[0,1,0]]
tub=[[0,1,0],[1,0,1],[0,1,0]]
line=[[0,0,0],[1,1,1],[0,0,0]]
toad=[[0,0,0,0],[0,1,1,1],[1,1,1,0],[0,0,0,0]]
beacon=[[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]] 
glider=[[0,0,1],[1,0,1],[0,1,1]]
glider2=[[0,1,1],[1,0,1],[0,0,1]]
glider3=[[1,1,0],[1,0,1],[1,0,0]]
glider4=[[1,0,0],[1,0,1],[1,1,0]]
rpentomino=[[0,1,1],[1,1,0],[0,1,0]]

width = 50
height = 40
frames = 1000
sleep_time = .01

grid = Grid(width, height)


grid.insert_seed(10,10,rpentomino)

# grid.insert_seed(10,10,beehive)
# grid.insert_seed(5,2,glider)
# grid.insert_seed(12,23,glider4)
# grid.insert_seed(20,7,glider2)
# grid.insert_seed(16,12,glider)
# grid.insert_seed(23,12,glider)


for _ in range(frames):
    os.system("clear")
    grid.out()
    grid.next()
    sleep(sleep_time)

