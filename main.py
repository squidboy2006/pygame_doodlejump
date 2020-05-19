#art from kenney.ln

import pygame as pg
import random
from settings import *
from sprites import *
from os import path
 
class Game: 
    def __init__(self):
        #initialize game window, ect
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
  
    def load_data(self):
        #load high score
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        #load spritesheet images
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        #load sounds
        self.snd_dir = path.join(self.dir, 'snd')
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Jump.wav'))
        self.jetpack_sound = pg.mixer.Sound(path.join(self.snd_dir, 'jetpack_powerup.wav'))

    def new(self):
        #starts a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.player = Player(self)
        for plat in PLATFORM_LIST:
            Platform(self, *plat)
        #this is what would be here if i had music
        #pg.mixer.music.load(path.join(self.snd, 'music_name.ogg'))

    def run(self):
        #game loop
        #this is what would be here if i had music
        #pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing == True:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        #pg.mixer.music.fadeout(1000)

    def update(self):
        #game loop - update 
        self.all_sprites.update()

        #check if player is on a platform only if falling
        if self.player.vel.y > 0:
            collisions = pg.sprite.spritecollide(self.player, self.platforms, False)
            if collisions:
                self.player.jumping = False
                lowest = collisions[0]
                for hit in collisions:
                    if hit.rect.bottom > lowest.rect.centery:
                        lowest = hit
                
                if self.player.pos.x < lowest.rect.right + 6 and \
                   self.player.pos.x > lowest.rect.left - 6:
                    if self.player.pos.y < lowest.rect.bottom:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.rect.midbottom = self.player.pos

        #if player reaches the top 1/4 of the screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                plat.rect.top += max(abs(self.player.vel.y), 2)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10
        #if player hits a powerup
        pow_collisions = pg.sprite.spritecollide(self.player, self.powerups, True)
        for p in pow_collisions:
            if p.type == 'boost':
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False
                self.jetpack_sound.play()
        
        # die when falls off the screen
        if self.player.rect.bottom >= HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 15)
                if sprite.rect.bottom <= 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        #spawn new platforms
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            Platform(self, random.randrange(0, WIDTH - width), random.randrange(-50, -25))

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
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def draw(self):
        #game loop - draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.draw_text(str(self.score), 25, WHITE, WIDTH / 2, 5)
        pg.display.flip()

    def show_start_screen(self):
        #game start screen
        #this is what would be here if i had music
        #pg.mixer.music.load(path.join(self.snd, 'music_name.ogg'))
        #pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH / 2 , HEIGHT / 2)
        self.draw_text("press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("high score: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()
        #pg.mixer.music.fadeout(1000)

    def show_go_screen(self):
        #game over/continue
        #this is what would be here if i had music
        #pg.mixer.music.load(path.join(self.snd, 'music_name.ogg'))
        #pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("Game over", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2 , HEIGHT / 2)
        self.draw_text("press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 48, WHITE, WIDTH / 2, HEIGHT / 2 + 66)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.highscore))
        else:  
            self.draw_text("high score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()
         #pg.mixer.music.fadeout(1000)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
            font = pg.font.Font(self.font_name, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x, y)
            self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()