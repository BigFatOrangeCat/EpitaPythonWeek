#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:24:10 2019

@author: jichenjiang
"""

import pygame, sys
from pygame.locals import *
import random

'''Hide From JAVA !'''

# Possibility of the events
def choice(seq, prob):
    p = random.random()
    for i in range(len(seq)):
        if sum(prob[:i]) < p < sum(prob[:i+1]):
            return seq[i]


# Player
class PlayerSprite(pygame.sprite.Sprite):
    speed = 10
    
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load('player.png').convert() # load function，return a surface object
        self.image.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.image.get_rect()
        
    def update(self, key):
        if key[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if key[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if key[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if key[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            
        # Limit the player in the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600
    
# Enemy
class EnemySprite(pygame.sprite.Sprite):
    speed = choice([1,3,5], [0.5, 0.4, 0.1])
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('java.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(820, random.randint(0, 600)))
        self.speed = random.randint(5, 15)

    def update(self):
        self.rect.move_ip(-self.speed, 0) # From the right to left
        if self.rect.right < 0:
            self.kill() # Built-in sprite method

# Clouds
class CloudSprite(pygame.sprite.Sprite):
    speed = choice([1,2], [0.8, 0.2])
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('cloud.png').convert()
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.image.get_rect(
            center = (random.randint(820,900),random.randint(0,600))
        )

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()


# Background
class BackgroundSprite(pygame.sprite.Sprite):

    def __init__(self, size):
        super().__init__()
        self.image = pygame.Surface(size)  # 
        self.image.fill((135, 206, 250)) # Wathet Blue
        self.rect = pygame.Rect(0, 0, *size)

    def update(self):
        pass
        

class Game():

    def __init__(self):
        # Initial the game
        pygame.init()

        # The size of the screen and creat the screen object
        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption("Escape from EPITA JAVA!")
        
        
        # Two customize event
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 1000) # Trigger : 1000 milliseconds
        self.ADDCLOUD = pygame.USEREVENT + 2        
        pygame.time.set_timer(self.ADDCLOUD, 1000)

        
        self.background = BackgroundSprite(self.size)
        self.player = PlayerSprite()

        
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        
        self.all_sprites.add(self.player)
    
    
    def run(self):
        # The main cycle of the screen
        while True:
             
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()       
                elif event.type == KEYDOWN:           
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()                
                elif event.type == self.ADDENEMY: # Customize event
                    new_enemy = EnemySprite()
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)
                elif event.type == self.ADDCLOUD: # Customize event
                    new_cloud = CloudSprite()
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)
            
            # Background
            self.screen.blit(self.background.image, self.background.rect)
            
            # Receive the keyboard button
            key = pygame.key.get_pressed()
            
            
            self.player.update(key)
            self.enemies.update()
            self.clouds.update()
            

            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, sprite.rect)
            
            # Colision detect
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.player.kill()
                #print('Game Over!')
            
            # update the frame
            pygame.display.flip()
        
        
        
if __name__ == '__main__':
    Game().run()
