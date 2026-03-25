from region import Region
from temperature import Temperature


region = Region(1, 2, 3)
print(region)  # Region(1, 2, 3)
region.height = -42  # Nonsense value
print(region)  # Region(-42, 2, 3)

t = Temperature(25)
print(t.celsius)  # 25
t.celsius = -300  # Nonsense value since it is below absolute zero
print(t.celsius)  # -300
