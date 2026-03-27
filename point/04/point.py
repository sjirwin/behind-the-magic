import math

from cached import CachedProperty


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @CachedProperty
    def r(self):
        print("Computing r ...")
        return math.sqrt(self.x**2 + self.y**2)

    @CachedProperty
    def theta(self):
        print("Computing theta ...")
        return math.atan2(self.y, self.x)
