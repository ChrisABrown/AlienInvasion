import pygame


class Rocket:
    """A class to represent a rocket."""

    def __init__(self, game):
        """Initialize the game character"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.rocket_speed = 1

        # Load the character and get its rect.
        self.image = pygame.transform.rotate(pygame.image.load('../images/ship.bmp'), 270)
        self.rect = self.image.get_rect()

        # Start the character in the middle of the screen at the bottom of the window.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact horizontal positon.
        self.x = self.rect.x
        self.y = self.rect.y

        # Updates the position of the rocket.

        # Movement flags for the rocket.
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the position of the rocket."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blithe(self):
        """Draw the character on the screen"""
        self.screen.blit(self.image, self.rect)




