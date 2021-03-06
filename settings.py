
# game options/settings
TITLE = "Jumpy"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "Highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

#platforms
PLATFORM_LIST = [(0, HEIGHT - 40), (WIDTH / 2 - 50, HEIGHT * 3 / 4),
                (125, HEIGHT - 280), (350, 200), (WIDTH / 2, 10)]

#player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = -23

#game properties
BOOST_POWER = 50
POWERUP_SPAWN_PCT = 7
MOB_FREQ = 5000

#game layers 
PLAYER_LAYER = 3
PLATFORM_LAYER = 1
POWERUP_LAYER = 2
MOB_LAYER = 3
CLOUD_LAYER = 0


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