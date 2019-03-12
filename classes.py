class Pos():
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Tile():
  def __init__(self, x, y, char, color, solid):
    self.x = x
    self.y = y
    self.char = char
    self.color = color
    self.solid = solid

class Player():
  def __init__(self, x, y, char, health):
    self.x = x
    self.y = y
    self.char = char
    self.health = health
    self.color = '193,25,25'

  def move(self, xv, yv, game_map):
    self.x += xv
    self.y += yv