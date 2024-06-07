import math
from const import *


class Point:
    """Class used for point objects"""
    def __init__(self, pos, pos2=None):
        #receive pos as (x,y)
        if pos2 is None:
            from road import Road
            self.pos = pos
            self.x, self.y = pos
            self.adjacents: list[tuple[Road, Point]] = []

        #receive x, y
        else:
            self.pos = (pos, pos2)
            self.x = pos
            self.y = pos2
            self.adjacents = []

    def _calc_dist(self, pos: tuple):
        """Calculate distance from this position to another position

        Parameter:
            :param pos(Tuple[int, int]): A tuple containing the (x,y) coordinates of the `pos` position
        """
        return math.dist(self.pos, pos)

    def _degree(self):
        """Return the point's degree = number of adjacents road"""
        return len(self.adjacents)

    def __eq__(self, _point: object):
        if self is None or _point is None:
            return (self is None) and (_point is None)
        return self.x == _point.x and self.y == _point.y

    def __str__(self):
        return f'{self.pos}'