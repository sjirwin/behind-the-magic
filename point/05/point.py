import math

from cached import CachedProperty, InvalidatingAttribute


class Point:
    x = InvalidatingAttribute()
    y = InvalidatingAttribute()

    # Cached polar coordinates
    r = CachedProperty(lambda self: self._r(), "x", "y")
    theta = CachedProperty(lambda self: self._theta(), "x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _r(self):
        print("Computing r ...")
        return math.sqrt(self.x**2 + self.y**2)

    def _theta(self):
        print("Computing theta ...")
        return math.atan2(self.y, self.x)
