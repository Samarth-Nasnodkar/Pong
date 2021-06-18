import math


def toDegrees(x):
    return int(x * 180 / math.pi)


class Vector2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __len__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(other * self.x, other * self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    @property
    def angle(self):
        ang = 90
        if self.x != 0:
            ang = toDegrees(math.atan(self.y / self.x))
        ang = ang if ang >= 0 else -1 * ang
        if self.x >= 0 <= self.y:
            return -1 * ang
        elif self.x <= 0 <= self.y:
            return ang - 180
        elif self.x < 0 >= self.y:
            return 90 + ang
        else:
            return ang

    @property
    def toTuple(self):
        return self.x, self.y
