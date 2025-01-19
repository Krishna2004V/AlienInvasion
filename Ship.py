import pygame

class Ship:
    """A Class To Manage The Ship"""
    def __init__(self, AI_Game):
        """Initialize The Ship And Set Its Starting Position"""
        self.screen = AI_Game.screen
        self.settings = AI_Game.Settings
        self.screen_rect = AI_Game.screen.get_rect()
        #Load The Ship Image And Get Its Rect
        self.image = pygame.image.load('Images/Ship.bmp')
        self.rect = self.image.get_rect()
        #Start Each New Ship At The Bottom Center of The Screen
        self.rect.midbottom = self.screen_rect.midbottom
        #Store A Float For The Ship's Exact Horizontal Position
        self.x = float(self.rect.x)
        #Movement Flags: Start With A Ship That's Not Moving
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Update The Ship's Position Based on The Movement Flags"""
        #Update The Ship's X Value, Not The Rect's
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #Update Rect Object From self.x
        self.rect.x = self.x
    def blitme(self):
        """Draw The Ship At Its Current Location"""
        self.screen.blit(self.image, self.rect)