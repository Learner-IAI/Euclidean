class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == type(self):
            return self.x * other.x + self.y * other.y
        return point(self.x * other, self.y * other)

    def __truediv__(self, other):
        return point(self.x / other, self.y / other)

    def is_right_of(self, other):
        det = self.x * other.y - self.y * other.x
        return 0 if det == 0 else det / abs(det)

    def reflect_about(self, other):
        return self + 2 * (other - self)


def rightest(pnt, points):
    res = points[0]
    for p in points[1:]:
        if (p - pnt).IsRightOf(pnt - res) > 0:
            res = p
    for p in points:
        if p is not res and (p - pnt).IsRightOf(pnt - res) == 0:
            return None
    return res
