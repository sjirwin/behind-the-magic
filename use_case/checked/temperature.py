_ABSOLUTE_ZERO = -273.15


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < _ABSOLUTE_ZERO:
            raise ValueError(f"Value must be >= {_ABSOLUTE_ZERO}")
        self._celsius = value
