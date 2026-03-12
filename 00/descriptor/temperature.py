from attribute import ValidatedAttribute


class Temperature:
    celsius = ValidatedAttribute(min_value=-273.15)  # Absolute zero

    def __init__(self, celsius):
        self.celsius = celsius


if __name__ == "__main__":
    t = Temperature(25)
    print(t.celsius)  # 25

    t.celsius = -300  # Raises ValueError: Value must be >= -273.15
