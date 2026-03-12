import math

from descriptor import CachedProperty, InvalidatingAttribute


class Point:
    x = InvalidatingAttribute()
    y = InvalidatingAttribute()

    # Cached polar coordinates
    r = CachedProperty(lambda self: math.sqrt(self.x**2 + self.y**2), "x", "y")
    theta = CachedProperty(lambda self: math.atan2(self.y, self.x), "x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    p = Point(3, 4)

    print(f"First access to r={p.r}")  # Calculates: 5.0
    print(f"Second access to r={p.r}")  # Cached: 5.0
    p.x = 5
    print(f"After changing x, r={p.r}")  # Recalculates: 6.403...
