from bearlibterminal import terminal
import esper
from components import *
from processes import *
from constants import *
from bresenham import *

# Create world and add processes
world = esper.World()
movement_processor = PlayerMovementProcessor()
rendering_processor = RenderProcess()
world.add_processor(movement_processor)
world.add_processor(rendering_processor)

# Create Player entity and add components
player = world.create_entity()
world.add_component(player, Velocity(0, 0))
world.add_component(player, Position())
world.add_component(player, Renderer('@', terminal))
world.add_component(player, Health(10))
world.add_component(player, IsPlayer("Player"))

def render():
  for y in range(0, GAME_HEIGHT):
    for x in range(0, GAME_WIDTH):
      terminal.printf(x, y, '.')
  # Info Panel
  for y in range(0, GAME_HEIGHT):
    for x in range(GAME_WIDTH, WINDOW_WIDTH):
      terminal.printf(x, y, ' ')

  terminal.refresh()

def handle_keys():
  global world
  key_input = terminal.read()

  if key_input == terminal.TK_Q or key_input == terminal.TK_CLOSE:
    return False
  elif key_input == terminal.TK_W:
    world.add_component(player, Velocity(0, -1))
  elif key_input == terminal.TK_S:
    world.add_component(player, Velocity(0, 1))
  elif key_input == terminal.TK_A:
    world.add_component(player, Velocity(-1, 0))
  elif key_input == terminal.TK_D:
    world.add_component(player, Velocity(1, 0))
  else:
    world.add_component(player, Velocity(0, 0))
  return True

def main():
  global world
  terminal.open()
  terminal.set("window.size = " + str(WINDOW_WIDTH) + "x" + str(GAME_HEIGHT))
  terminal.set("font: square.ttf, size=14;")
  
  # terminal.set("U+E500: ./Media/test.png, resize=128x128, resize-filter=nearest")
  # terminal.set("U+E000: ./at.png")
  # terminal.set("U+E100: ./period.png")
  # terminal.set("U+E200: ./question.png")

  playing = True

  render()

  while playing:

    playing = handle_keys()

    render()

    world.process()

  terminal.close()

if __name__ == '__main__':
  main()