from bearlibterminal import terminal
from classes import *
from gen import *
from constants import *
from bresenham import *

wild_gen = WildernessGenerator(GAME_WIDTH, GAME_HEIGHT)

# Create Player entity and add components
player = Player(5, 5, '@', 10)

game_map = None

def draw_char(x, y, char, color, layer):
  old_layer = terminal.TK_LAYER
  old_color = terminal.TK_COLOR
  terminal.layer(layer)
  terminal.color(color)
  terminal.printf(x, y, char)
  terminal.color(old_color)
  terminal.layer(old_layer)

def render():
  global player, game_map

  for y in range(0, GAME_HEIGHT):
    for x in range(0, GAME_WIDTH):
      t = game_map[x][y]
      draw_char(t.x, t.y, t.char, t.color, 0)

  # Info Panel
  for y in range(0, GAME_HEIGHT):
    for x in range(GAME_WIDTH, WINDOW_WIDTH):
      terminal.printf(x, y, ' ')

  draw_char(player.x, player.y, player.char, player.color, 0)

  terminal.refresh()

def handle_keys():
  global player, game_map
  key_input = terminal.read()

  if key_input == terminal.TK_Q or key_input == terminal.TK_CLOSE:
    return False
    
  elif key_input == terminal.TK_W:
    if not game_map[player.x][player.y-1].solid:
      player.move(0, -1, [[]])
      
  elif key_input == terminal.TK_S:
    if not game_map[player.x][player.y+1].solid:
      player.move(0, 1, [[]])
      
  elif key_input == terminal.TK_A:
    if not game_map[player.x-1][player.y].solid:
      player.move(-1, 0, [[]])
      
  elif key_input == terminal.TK_D:
    if not game_map[player.x+1][player.y].solid:
      player.move(1, 0, [[]])
      
  else:
    player.move(0, 0, [[]])

  if (key_input == terminal.TK_SPACE):
    game_map = wild_gen.gen()

  return True

def main():
  global game_map

  terminal.open()
  terminal.set("window.size = " + str(WINDOW_WIDTH) + "x" + str(GAME_HEIGHT))
  terminal.set("font: square.ttf, size=14;")
  
  # terminal.set("U+E500: ./Media/test.png, resize=128x128, resize-filter=nearest")
  # terminal.set("U+E000: ./at.png")
  # terminal.set("U+E100: ./period.png")
  # terminal.set("U+E200: ./question.png")

  game_map = wild_gen.gen()

  playing = True

  render()

  while playing:

    playing = handle_keys()

    render()

  terminal.close()

if __name__ == '__main__':
  main()