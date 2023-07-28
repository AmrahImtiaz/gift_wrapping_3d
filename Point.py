import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        """Calculate the length (magnitude) of the vector from the origin to the point."""
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __eq__(self, other):
        """Check if two points are equal."""
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __lt__(self, other):
        """Define the less-than comparison for points based on their x, y & z coordinates."""
        return (self.z < other.z) or (self.y < other.y) or (self.x < other.x)

    def __sub__(self, other):
        """Subtract another point from this point."""
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        """Add another point to this point."""
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __truediv__(self, number):
        """Divide the point's coordinates by a non-zero number."""
        if number == 0:
            return None

        return Point(self.x / number, self.y / number, self.z / number)

    def __mul__(self, number):
        """Multiply the point by a scalar number."""
        return Point(self.x * number, self.y * number, self.z * number)

    def __hash__(self):
        """Calculate the hash value for the point, used for hashing in sets and dictionaries."""
        return int((self.x + self.y ** 2 + self.z ** 3) % 100)
