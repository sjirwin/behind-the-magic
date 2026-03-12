class Region:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def __str__(self):
        return f"height={self.height}, width={self.width}, depth={self.depth}"

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError(f"Value must be >= 0")
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError(f"Value must be >= 0")
        self._width = value

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        if value < 0:
            raise ValueError(f"Value must be >= 0")
        self._depth = value


if __name__ == "__main__":
    region = Region(1, 2, 3)
    print(region)  # height=1, width=2, depth=3

    region.height = -42  # Raises ValueError: Value must be >= 0
