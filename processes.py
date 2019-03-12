import esper
from components import *

class PlayerMovementProcessor(esper.Processor):
  def __init__(self):
    super().__init__()

  def process(self):
    for _, (vel, pos) in self.world.get_components(Velocity, Position):
      pos.x += vel.vx
      pos.y += vel.vy

class RenderProcess(esper.Processor):
  def __init__(self):
    super().__init__()

  def process(self):
    for _, (pos, ren) in self.world.get_components(Position, Renderer):
      ren.target.printf(pos.x, pos.y, '@')
      ren.target.refresh()