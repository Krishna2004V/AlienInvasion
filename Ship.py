import pygame

class Ship:
    """A Class To Manage The Ship"""
    def __init__(self, AI_Game):
        """Initialize The Ship And Set Its Starting Position"""
        self.screen = AI_Game.screen
        self.screen_rect = AI_Game.screen.get_rect()
        #Load The Ship Image And Get Its Rect
        self.image = pygame.image.load('Images/Ship.bmp')
        self.rect = self.image.get_rect()
        #Start Each New Ship At The Bottom Center of The Screen
        self.rect.midbottom = self.screen_rect.midbottom
        #Movement Flags: Start With A Ship That's Not Moving
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Update The Ship's Position Based on The Movement Flags"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
    def blitme(self):
        """Draw The Ship At Its Current Location"""
        self.screen.blit(self.image, self.rect)