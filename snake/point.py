class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def point(self):
        point = [self.x, self.y]
        return point

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def change_point(self, x, y):
        self._x = x
        self._y = y

    def move_x_right(self):
        self._x += 1

    def move_x_left(self):
        self._x -= 1

    def move_y_down(self):
        self._y +=1

    def move_y_up(self):
        self._y -=1
