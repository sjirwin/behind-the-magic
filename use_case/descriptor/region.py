from attribute import ValidatedAttribute


class Region:
    height = ValidatedAttribute(min_value=0)
    width = ValidatedAttribute(min_value=0)
    depth = ValidatedAttribute(min_value=0)

    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def __repr__(self):
        return f"Region({self.height}, {self.width}, {self.depth})"
