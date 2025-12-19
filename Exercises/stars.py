import sys
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star."""
    def __init__(self, game):
        """Initialize the star and set its position."""
        super().__init__()
        self.screen = game.screen

        self.image = pygame.image.load('../images/retro_star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


class Stars:
    """Class to set up Exercise 13-1"""
    def __init__(self):
        """Initialize the game and set up resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        screen_height = 800
        screen_width = 600
        self.screen = pygame.display.set_mode((screen_height, screen_width))

        pygame.display.set_caption('Stars')

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """Run the game"""
        while True:
            self._create_stars()
            self.check_events()
            self._create_stars()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """Update the screen"""
        self.screen.fill('white')
        self.stars.draw(self.screen)

        pygame.display.flip()

    def check_events(self):
        """Check for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.close_game(event)

    def close_game(self, event):
        """Close the game"""
        if event.type == pygame.KEYDOWN:
            pass
        if event.key == pygame.K_ESCAPE:
                sys.exit()


    def _create_stars(self):
        """Create the stars"""
        star = Star(self)
        self.stars.add(star)

    def _create_star(self, x, y):
        """Create the star"""
        new_star = Star(self)
        new_star.x = x
        new_star.rect.x = x
        new_star.rect.y = y

if __name__ == '__main__':
    game = Stars()
    game.run_game()