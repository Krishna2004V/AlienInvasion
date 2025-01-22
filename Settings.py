class Settings:
    """A Class To Store All The Settings For The Game"""
    def __init__(self):
        """Initialize The Game's Settings"""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (225, 225, 225)
        #Ship Settings
        self.ship_speed = 1.5
        #Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        #Alien Settings
        self.alien_speed = 1.0