from classes import *
from random import *
from constants import *

class WildernessGenerator:
  def __init__(self, w, h):
    self.width = w
    self.height = h

  def gen(self):
    wilderness_map = [[ Tile(x, y, ';', '122,150,40', False)
        for y in range(0, self.height) ]
            for x in range(0, self.width) ]

    taken_spots = []

    num_of_trees = randint(8, 20)

    for _ in range(0, num_of_trees):
      x = randint(1, GAME_WIDTH-2)
      y = randint(1, GAME_HEIGHT-2)
      t = Tile(x, y, '#', '102,71,14', True)
      wilderness_map[x][y] = t

    num_of_rocks = randint(4, 6)

    for _ in range(0, num_of_rocks):
      x = randint(1, GAME_WIDTH-2)
      y = randint(1, GAME_HEIGHT-2)
      r = Tile(x, y, '0', 'light grey', True)
      wilderness_map[x][y] = r

    return wilderness_map