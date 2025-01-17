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
    def _check_event(self):
        #Respond To Keyboard And Mouse Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def run_game(self):
        """Start The Main Loop For The Game"""
        while True:
            self._check_event()
            #Redraw The Screen During Each Pass Through The Loop
            self.screen.fill(self.Settings.bg_color)
            self.Ship.blitme()
            #Make The Most Recently Drawn Screen Visible
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == '__main__':
    #Make A Game Instance, And Run The Game
    AI = AlienInvasion()
    AI.run_game()