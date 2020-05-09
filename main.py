import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        #initialize game window, ect
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #starts a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

    def run(self):
        #game loop
        self.playing = True
        while self.playing == True:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #game loop - update
        self.all_sprites.update()
        #check if player is on a platform only if falling
        if self.player.vel.y > 0:
            collisions = pg.sprite.spritecollide(self.player, self.platforms, False)
            if collisions:
                self.player.pos.y = collisions[0].rect.top
                self.player.vel.y = 0
                self.player.rect.midbottom = self.player.pos
        #if player reaches the top 1/4 of the screen
        print (self.player.rect.top <= HEIGHT / 4.5)
        if self.player.rect.top <= HEIGHT / 4.5:
            self.player.rect.y += 18.5
            for plat in self.platforms:
                plat.rect.y += WINDOW_SCROLL
                if plat.rect.top >= HEIGHT:
                    plat.kill()
        #spawn new platforms
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width), random.randrange(-50, -25), width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        #game loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing == True:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        #game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        #game start screen
        pass

    def show_go_screen(self):
        #game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()