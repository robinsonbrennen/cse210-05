import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):

    def __init__(self, color):
        super().__init__()
        self._cycle_color = color
        self._segments = []
        self._prepare_body()
        
    def get_segments(self):
        return self._segments

    def move_next(self):
        for segment in self._segments:
            segment.move_next()
            
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._cycle_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = 0.0
        y = 0.0

        if self._cycle_color == constants.CYAN:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
        else:
            x = int(constants.MAX_X / 4)
            y = int(constants.MAX_Y / 4)
        

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._cycle_color)
            self._segments.append(segment)