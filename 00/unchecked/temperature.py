class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius


if __name__ == "__main__":
    t = Temperature(25)
    print(t.celsius)  # 25
    t.celsius = -300  # Invalid. Below absolute zero
