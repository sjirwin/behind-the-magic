class Region:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def __str__(self):
        return f"height={self.height}, width={self.width}, depth={self.depth}"


if __name__ == "__main__":
    region = Region(1, 2, 3)
    print(region)  # height=1, width=2, depth=3

    region.height = -42
    print(region)  # height=-42, width=2, depth=3
