import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.
    Attributes:
        _cycle_color - Color of the cycle
    """
    def __init__(self, color, position):
        super().__init__()
        self._cycle_color = color
        # setting cycle positions
        self._segments = []
        self._head = Actor()
        self._head.set_color(color)
        self._head.set_text('@')
        self._head.set_position(position)
        self._segments.append(self._head)
        
        
    def get_segments(self):
        return self._segments

    def move_next(self):
        # Makes the cylces Move
        self._segments[0].move_next()
        # update velocities
        self._tail = Actor()
        self._tail.set_color(self._cycle_color)
        self._tail.set_text('#')
        self._segments.append(self._tail)
        self._tail.set_position(self._head.get_position())
                
        

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
            segment.set_text('#')
            segment.set_color(constants.GREEN)
            self._segments.append(segment)




    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self):
        x = int(constants.MAX_X /2)
        Y = int(constants.MAX_Y / 2)

        if (self._cycle_color == constants.GREEN):
            x += 600
            y -= 100
        else:
            x -= 600
            y += 100

        for i in range(constants.SNAKE_LENGHT):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(0, 1 * constants.CELL_SIZE, 0)
            text = '8' if i == 0 else '#'
            if (self._cycle_color == constants.GREEN):
                color = constants.GREEN
            else:
                color = constants.RED

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.get_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    