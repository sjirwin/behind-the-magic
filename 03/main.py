from point import Point


p = Point(3, 4)

print(f"First access to r={p.r}")  # Calculates: 5.0
print(f"Second access to r={p.r}")  # Cached: 5.0

p.x = 5
print(f"After changing x, r={p.r}")  # Invalid cached value
