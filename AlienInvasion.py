import sys
import pygame

from Settings import Settings
from Ship import Ship
from Bullet import Bullet
from Alien import Alien

class AlienInvasion:
    """OverAll Class To Manage Game Assets And Behaviour"""
    def __init__(self):
        """Initialize The Game, And Create Game Resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.Settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.Settings.screen_width = self.screen.get_rect().width
        self.Settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(("Alien Invasion"))
        self.Ship = Ship(self)
        self.Bullets = pygame.sprite.Group()
        self.Aliens = pygame.sprite.Group()
        self._create_fleet()
    def _create_alien(self, x_position, y_position):
        """Create An Alien And Place It in The Row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.Aliens.add(new_alien)
    def _create_fleet(self):
        """Create The Fleet of Aliens"""
        #Create An Alien And Keep Adding Aliens Until There's No Room Left
        #Spacing Between Aliens is One Alien Width And One Alien Height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.Settings.screen_height - 3 * alien_height):
            while current_x < (self.Settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #Finished A Row
            #Reset The Value of X And Increment The Value of Y
            current_x = alien_width
            current_y += 2 * alien_height
        #Set The Background Colour
        self.bg_color = (225, 225, 225)
    def _update_aliens(self):
        """Update The Positions of All Aliens in The Fleet"""
        self.Aliens.update()
    def _fire_bullet(self):
        """Create A New Bullet And Add It To The Bullets Group"""
        if len(self.Bullets) < self.Settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.Bullets.add(new_bullet)
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
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.Ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.Ship.moving_left = False
    def _update_bullets(self):
        """Update Position of Bullets And Get Rid of The Old Bullets"""
        #Update Bullet Positions
        self.Bullets.update()
        #Get Rid of Bullets That Have Disappeared
        for bullet in self.Bullets.copy():
            if bullet.rect.bottom <= 0:
                self.Bullets.remove(bullet)
    def _update_screen(self):
        """Update Images on The Screen, And Flip To The New Screen"""
        self.screen.fill(self.Settings.bg_color)
        for bullet in self.Bullets.sprites():
            bullet.draw_bullet()
        self.Ship.blitme()
        self.Aliens.draw(self.screen)
        pygame.display.flip()
    def run_game(self):
        """Start The Main Loop For The Game"""
        while True:
            self._check_events()
            self.Ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
if __name__ == '__main__':
    #Make A Game Instance, And Run The Game
    AI = AlienInvasion()
    AI.run_game()