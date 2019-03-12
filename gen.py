from classes import *

class WildernessGenerator:
  def __init__(self, w, h):
    self.width = w
    self.height = h
    self.tiles = []

  def gen(self):
    wilderness_map = [[ Tile(x, y, '.')
        for y in range(self.height) ]
            for x in range(self.width) ]
      