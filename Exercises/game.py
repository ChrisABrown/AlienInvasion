import pygame
import sys

from rocketship import Rocket
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = ai_game.rocket.rect.midright

        # Store the bullet's position as a float
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen to the right."""
        # Update the exact position of the bullet.
        self.x += self.bullet_speed

        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)


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


class Enemy(Sprite):
    def __init__(self, ai_game):
        """A class to manage enemies at fired from the ship."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        image = pygame.image.load('../images/retro_star.png').convert_alpha()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.settings = GameSettings()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.y -= self.settings.armada_speed * self.settings.armada_direction
        self.rect.y = self.y

    def check_edges(self):
        top = self.screen.get_rect().top
        bottom = self.screen.get_rect().bottom
        return (self.rect.y >= bottom) or (self.rect.y >= top)

class GameSettings:
    """Class to manage the game settings."""
    def __init__(self):
        """Initialize the game settings."""
        self.screen_width = 1200
        self.screen_height = 800

        self.armada_speed = 0.5
        self.armada_drop_speed = 0.005
        self.armada_direction = -1


class VideoGame:
    """A class to manage a game"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bullets_allowed = 3
        self.settings = GameSettings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.armada = pygame.sprite.Group()

        # Change this to change the icon that shows up.
        # self.player_image = Rocket(self)

        # collisions = pygame.sprite.spritecollide(self.rocket, self.bullets, True)
        pygame.display.set_caption("Game")

        self._create_armada()

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self.rocket.update()
            self._update_armada()
            self._update_bullets()
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

    def _fire_bullet(self):
        """Fire a bullet from the rocket."""
        if len(self.bullets) < self.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)

    def _check_keydown_events(self, event):
        """Check for keyboard presses."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rocket.moving_left = True
            elif event.key == pygame.K_RIGHT:
                self.rocket.moving_right = True
            elif event.key == pygame.K_UP:
                self.rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.rocket.moving_down = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
            elif event.key == pygame.K_q:
                sys.exit()

    def _check_keyup_events(self, event):
        """Check for keyboard releases."""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.rocket.moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.rocket.moving_right = False
            elif event.key == pygame.K_UP:
                self.rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.rocket.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill((230, 230, 230))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blithe()
        self.armada.draw(self.screen)

        pygame.display.flip()

    def _create_armada(self):
        enemy = Enemy(self)
        enemy_height, enemy_width = enemy.rect.size

        current_y, current_x = enemy_height, enemy_width
        while current_x < (self.settings.screen_width - 6 * enemy_width):
            while current_y < (self.settings.screen_height - 2 * enemy_height):
                self._create_enemy(current_x, current_y)
                current_y += 2  * enemy_height

            current_y = enemy_height
            current_x += 2 * enemy_width

    def _create_enemy(self, x, y):
        new_enemy = Enemy(self)
        new_enemy.y = y
        new_enemy.rect.y =  y
        new_enemy.rect.right = x + self.settings.screen_width // 2
        self.armada.add(new_enemy)

    def _update_armada(self):
        self._check_armada_edges()
        self.armada.update()

    def _check_armada_edges(self):
        for enemy in self.armada.sprites():
            if enemy.check_edges():
                self._change_armada_direction()
                break

    def _change_armada_direction(self):
        for enemy in self.armada.sprites():
            enemy.rect.x += self.settings.armada_drop_speed
        self.settings.armada_direction *= -1



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = VideoGame()
    ai.run_game()
