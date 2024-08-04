from pygame import *
from random import *
from time import time as timer
font.init()
font1 = font.SysFont("mvboli", 50)
font2 = font.SysFont("mvboli", 380)

life = 3
num_fire = 0
rel_time = False
num_fire2 = 0
rel_time2 = False


win = display.set_mode((1280, 720))
display.set_caption("Cnhtktkre")
background = transform.scale(image.load("bg2.png"), (1280, 720))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, playeк_width, player_hight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (playeк_width, player_hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 1210:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 605:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet("b1.png", self.rect.centerx, self.rect.top, -20, 10, 20)
        bullets.add(bullet)
    def supercharge(self):
        charge = Bullet("b2.png", self.rect.centerx, self.rect.top, -20, 80, 160)
        charges.add(charge)

    

score = 0
lost = 0
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.rect.y = -80
            self.rect.x = randint(0, 1210)
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < -20:
            self.kill()




charges = sprite.Group()
bullets = sprite.Group()
enemies1 = sprite.Group()
enemies2 = sprite.Group()
enemies3 = sprite.Group()
enemies4 = sprite.Group()
enemies5 = sprite.Group()

for i in range(2):
    enemy = Enemy("enemy1.png", randint(0, 1210), -80, randint(2, 5), 50, 70)
    enemies1.add(enemy)
for i in range(2):
    enemy = Enemy("enemy2.png", randint(0, 1210), -80, randint(1, 2), 50, 60)
    enemies2.add(enemy)
for i in range(1):
    enemy = Enemy("enemy3.png", randint(0, 1210), -80, randint(1, 2), 70, 70)
    enemies3.add(enemy)
for i in range(1):
    enemy = Enemy("boss3.png", randint(0, 1210), -80, randint(1, 2), 100, 140)
    enemies4.add(enemy)
for i in range(2):
    enemy = Enemy("meteor2_3.png", randint(0, 1210), -80, randint(1, 1), 90, 65)
    enemies5.add(enemy)
boss = Enemy("boss.png", 600, -80, 1, 250, 140)
enemies4.add(enemy)
player = Player("player.png", 400, 400, 20, 75, 110)



 

mixer.init()
mixer.music.load("bg_m.ogg")
mixer.music.play()
mixer.music.set_volume(0.1)
hit = mixer.Sound("shoots.ogg")


finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <5 and rel_time == False:
                    player.fire()
                    hit.play()
                    num_fire = num_fire + 1
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True 
                    

            if e.key == K_e:
                if num_fire2 < 2 and rel_time2 == False:
                    player.supercharge()
                    hit.play()
                    pods = 31
                    num_fire2 = num_fire2 + 1
                if num_fire2 >= 2 and rel_time2 == False:
                    last_time2 = timer()
                    rel_time2 = True 
                

    if finish != True:
        win.blit(background, (0, 0))
        text_lose = font1.render("Lost:" + str(lost), 1, (208, 235, 245))
        text_score = font1.render("Score:" + str(score), 1, (208, 235, 245))
        win.blit(text_lose, (0, 0))
        win.blit(text_score, (0, 50))
        enemies1.draw(win)
        enemies1.update()
        enemies2.draw(win)
        enemies2.update()
        enemies3.draw(win)
        enemies3.update()
        enemies4.draw(win)
        enemies4.update()
        enemies5.draw(win)
        enemies5.update()
        player.reset()
        player.update()
        bullets.draw(win)
        bullets.update()
        charges.draw(win)
        charges.update()

        if rel_time == True:
            new_time = timer()
            if new_time - last_time <= 3:
                pass
            else:
                num_fire = 0
                rel_time = False

        if rel_time2 == True:
            new_time2 = timer()
            if new_time2 - last_time2 <= 3:
                pass
            else:
                num_fire2 = 0
                rel_time2 = False



    
        collides = sprite.groupcollide(enemies1, bullets, True, True) or sprite.groupcollide(enemies1, charges, True, True)
        for _ in collides:
            score = score +1
            enemy = Enemy("enemy1.png", randint(0, 1210), -80, randint(1, 5), 50, 70)
            enemies1.add(enemy)

        collides = sprite.groupcollide(enemies2, bullets, True, True) or sprite.groupcollide(enemies2, charges, True, True)
        for _ in collides:
            score = score +1
            enemy = Enemy("enemy2.png", randint(0, 1210), -80, randint(1, 5), 50, 60)
            enemies2.add(enemy)
            
        collides = sprite.groupcollide(enemies3, bullets, True, True) or sprite.groupcollide(enemies3, charges, True, True)
        for _ in collides:
            score = score +1
            enemy = Enemy("enemy3.png", randint(0, 1210), -80, randint(1, 5), 70, 70)
            enemies3.add(enemy)

        collides = sprite.groupcollide(enemies5, charges, True, True)
        for _ in collides:
            score = score +1
            enemy = Enemy("meteor2_3.png", randint(0, 1210), -80, randint(1, 5), 70, 70)
            enemies5.add(enemy)

        
        collides = sprite.groupcollide(enemies4, charges, True, True)
        for _ in collides:
            score = score +1
            enemy = Enemy("boss3.png", randint(0, 1210), -80, randint(1, 4), 100, 140)
            enemies4.add(enemy)
        if sprite.spritecollide(player, enemies4, False) or sprite.spritecollide(player, enemies3, False) or sprite.spritecollide(player, enemies2, False) or sprite.spritecollide(player, enemies1, False) or sprite.spritecollide(player, enemies5, False):
            sprite.spritecollide(player, enemies4, True)
            sprite.spritecollide(player, enemies3, True)
            sprite.spritecollide(player, enemies2, True)
            sprite.spritecollide(player, enemies1, True)
            sprite.spritecollide(player, enemies5, True)
            life -= 1
                
        if score > 10:
            wintext = font2.render("Pabeda", True, (208, 235, 245))
            win.blit(wintext, (0, 0))
            finish = True
            mixer.music.stop()
        
            
        
        if life == 0 or lost >=10:
            loosetext = font2.render("Smert(", True, (208, 235, 245))
            win.blit(loosetext, (0, 0))
            finish = True
            mixer.music.stop()

        if life == 3:
            img = "3.png"
        if life == 2:
            img = "2.png"
        if life == 1:
            img = "1.png"
        lifes = transform.scale(image.load(img), (420, 150))
        win.blit(lifes, (900, 0))

        display.update()


    else:
        finish = False
        score = 0
        num_fire = 0
        num_fire2 = 0
        lost = 0
        life = 3
        
        for a in charges:
            a.kill()
        for b in bullets:
            b.kill()
        for c in enemies1:
            c.kill()
        for c in enemies2:
            c.kill()
        for c in enemies3:
            c.kill()
        for c in enemies4:
            c.kill()
        for c in enemies5:
            c.kill()

        time.delay(3000)
        for i in range(2):
            enemy = Enemy("enemy1.png", randint(0, 1210), -80, randint(1, 2), 50, 70)
            enemies1.add(enemy)
        for i in range(2):
            enemy = Enemy("enemy2.png", randint(0, 1210), -80, randint(1, 2), 50, 60)
            enemies2.add(enemy)
        for i in range(1):
            enemy = Enemy("enemy3.png", randint(0, 1210), -80, randint(1, 2), 70, 70)
            enemies3.add(enemy)
        for i in range(1):
            enemy = Enemy("boss3.png", randint(0, 1210), -80, randint(1, 2), 100, 140)
            enemies4.add(enemy)
        for i in range(2):
            enemy = Enemy("meteor2_3.png", randint(0, 1210), -80, randint(1, 1), 90, 65)
            enemies5.add(enemy)
        boss = Enemy("boss.png", 600, -80, 1, 250, 140)
        enemies4.add(enemy)
        



    
    time.delay(8)
