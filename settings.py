
# game options/settings
TITLE = "Jumpy"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "Highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

#platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40), (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                (125, HEIGHT - 280, 100, 20), (350, 200, 90, 20), (WIDTH / 2, 10, 50, 20)]

#player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = -18.5

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
LIGHT_BLUE = (0, 155, 155)
BGCOLOR = LIGHT_BLUE