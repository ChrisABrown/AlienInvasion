import json
from pathlib import Path

class GameStats:
    """Track statistics about the game."""
    def __init__(self, ai_game):
        """Initialize the game statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self.save_high_score()


    def reset_stats(self):
        """Initialize the game statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save the high score."""
        path = Path('high_score.json')
        try:
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0
