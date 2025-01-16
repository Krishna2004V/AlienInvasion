import sys
import pygame

class AlienInvasion:
    """OverAll Class To Manage Game Assets And Behaviour"""
    def __init__(self):
        """Initialize The Game, And Create Game Resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption(("Alien Invasion"))
    def run_game(self):
        """Start The Main Loop For The Game"""
        while True:
            #Watch For Keyboard And Mouse Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Watch The Most Recently Drawn Screen Visible
            pygame.display.flip()
if __name__ == '__main__':
    #Make A Game Instance, And Run The Game
    AI = AlienInvasion()
    AI.run_game()