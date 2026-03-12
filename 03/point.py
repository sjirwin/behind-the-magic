import math
from functools import cached_property


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @cached_property
    def r(self):
        print("Computing r ...")
        return math.sqrt(self.x**2 + self.y**2)

    @cached_property
    def theta(self):
        print("Computing theta ...")
        return math.atan2(self.y, self.x)


if __name__ == "__main__":
    p = Point(3, 4)

    print(f"First access to r={p.r}")  # Calculates: 5.0
    print(f"Second access to r={p.r}")  # Cached: 5.0
    p.x = 5
    print(f"After changing x, r={p.r}")  # Invalid cached value
