from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _player (str): Identifies the player to display the score.
        _points (int): The points earned in the game.
        _position: The position to display the score.

    """
    def __init__(self, position, player):
        super().__init__()
        self._player = player
        self._points = 0
        self.add_points(0)
        self._position = position

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._player}: {self._points}")