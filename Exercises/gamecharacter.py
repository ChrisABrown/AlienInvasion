import pygame
import sys
from rocketship import Rocket


class GameCharacter:
    """A simple class to manage a game character"""
    def __init__(self, game):
        """Initialize the game character"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        #Load the character and get its rect.
        self.image = pygame.image.load('../images/snail.bmp')
        self.rect = self.image.get_rect()

        #Start the character in the middle of the screen.
        self.rect.center = self.screen_rect.center

    def blithe(self):
        """Draw the character on the screen"""
        self.screen.blit(self.image, self.rect)

class Game:
    """A class to manage a game"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()

        # Change this to change the icon that shows up.
        self.player_image = Rocket(self)

        pygame.display.set_caption("Game")

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self.player_image.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Check for keyboard events and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Check for keyboard presses."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player_image.moving_left = True
            elif event.key == pygame.K_RIGHT:
                self.player_image.moving_right = True
            elif event.key == pygame.K_UP:
                self.player_image.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.player_image.moving_down = True
            elif event.key == pygame.K_q:
                sys.exit()

    def _check_keyup_events(self, event):
        """Check for keyboard releases."""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player_image.moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.player_image.moving_right = False
            elif event.key == pygame.K_UP:
                self.player_image.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.player_image.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill('white')
        self.player_image.blithe()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Game()
    ai.run_game()
