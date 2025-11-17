from alien_invasion import AlienInvasion
from settings import Settings
from ship import Ship

newgame = AlienInvasion()
bluesky = Settings()
newgame.ship = Ship(newgame)
bluesky.bg_color = (0, 0, 255)


newgame.settings.bg_color = bluesky.bg_color
newgame.run_game()