import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A Class To Represent A Single Alien in The Fleet"""
    def __init__(self, AI_Game):
        super().__init__()
        self.screen = AI_Game.screen
        self.Settings = AI_Game.Settings
        #Load The Alien Image And Set Its Rect Attribute
        self.image = pygame.image.load('Images/Alien.bmp')
        self.rect = self.image.get_rect()
        #Start Each New Alien Near The Top Left of The Screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Store The Alien's Exact Horizontal Position
        self.x = float(self.rect.x)
    def update(self):
        """Move The Alien To The Right"""
        self.x += self.Settings.alien_speed
        self.rect.x = self.x