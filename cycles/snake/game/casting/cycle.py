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



    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)