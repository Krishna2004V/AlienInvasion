import sys
import pygame

from Settings import Settings
from Ship import Ship

class AlienInvasion:
    """OverAll Class To Manage Game Assets And Behaviour"""
    def __init__(self):
        """Initialize The Game, And Create Game Resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.Settings = Settings()
        self.screen = pygame.display.set_mode((self.Settings.screen_width, self.Settings.screen_height))
        pygame.display.set_caption(("Alien Invasion"))
        self.Ship = Ship(self)
        #Set The Background Colour
        self.bg_color = (225, 225, 225)
    def _check_events(self):
        #Respond To Keyboard And Mouse Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.Ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.Ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.Ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.Ship.moving_left = False
    def _update_screen(self):
        """Update Images on The Screen, And Flip To The New Screen"""
        self.screen.fill(self.Settings.bg_color)
        self.Ship.blitme()
        pygame.display.flip()
    def run_game(self):
        """Start The Main Loop For The Game"""
        while True:
            self._check_events()
            self.Ship.update()
            self._update_screen()
            self.clock.tick(60)
if __name__ == '__main__':
    #Make A Game Instance, And Run The Game
    AI = AlienInvasion()
    AI.run_game()