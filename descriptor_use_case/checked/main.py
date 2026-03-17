from region import Region
from temperature import Temperature


region = Region(1, 2, 3)
print(region)  # Region(1, 2, 3)
try:
    region.height = -42  # ValueError: Value must be >= 0
except ValueError as e:
    print(f"ValueError: {e}")

t = Temperature(25)
print(t.celsius)  # 25
try:
    t.celsius = -300  # ValueError: Value must be >= -273.15
except ValueError as e:
    print(f"ValueError: {e}")
