from attribute import ValidatedAttribute


class Temperature:
    celsius = ValidatedAttribute(min_value=-273.15)  # Absolute zero

    def __init__(self, celsius):
        self.celsius = celsius
