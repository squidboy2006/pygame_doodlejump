#sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2
class Spritesheet:
    #class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()
    
    def get_image(self, x, y, width, height):
        #grab an image from the spritesheet
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = self.game.spritesheet.get_image(614, 1063, 120, 191)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, 500)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        #jump onyl if standing on a platform
        self.rect.y += 1
        collision = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if collision:
            self.vel.y = PLAYER_JUMP

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        
        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #equation of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #wrap around the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
