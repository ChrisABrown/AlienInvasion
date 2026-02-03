class GameStats:
    """Track statistics about the game."""
    def __init__(self, ai_game):
        """Initialize the game statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize the game statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0

