class Position:
  def __init__(self, x=5, y=5):
    self.x = x
    self.y = y

class Velocity:
  def __init__(self, vx=0, vy=0):
    self.vx = vx
    self.vy = vy

class Renderer:
  def __init__(self, char, target):
    self.char = char
    self.target = target

class Health:
  def __init__(self, max_health):
    self.health = max_health
    self.max_health = max_health

class IsPlayer:
  def __init__(self, name):
    self.name = name
  
class Solid:
  def __init__(self):
    pass