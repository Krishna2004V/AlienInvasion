import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class To Manage Bullets Fired From The Ship"""
    def __init__(self, AI_Game):
        """Create A Bullet Object At The Ship's Current Position"""
        super().__init__()
        self.screen = AI_Game.screen
        self.settings = AI_Game.Settings
        self.color = self.settings.bullet_color
        #Create A Bullet Rect At (0,0) And Then Set Correct Position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = AI_Game.Ship.rect.midtop
        #Store The Bullet's Position As A Float
        self.y = float(self.rect.y)
    def update(self):
        """Move The Bullet Up The Screen"""
        #Update The Exact Position of The Bullet
        self.y -= self.settings.bullet_speed
        #Update The Rect Position
        self.rect.y = self.y
    def draw_bullet(self):
        """Draw The Bullet on The Screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)