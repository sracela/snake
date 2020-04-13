import copy
from state import State
from point import Point

head = Point(0,0)
class Snake:

    def __init__(self, head, snake_size):
        self.snake = [0] * snake_size
        head = Point(head.x, head.y)
        for i in range(snake_size):
            self.snake[i] = Point(head.x - i, head.y)

    @property
    def snake_size(self):
        return len(self.snake)

    @property
    def head(self):
        return self.snake[0]

    @property
    def body(self):
        return self.snake[1:]

    def grow(self):
        self.snake.append(self.snake[-1])

    def move(self, state):
        new_body = copy.deepcopy(self.snake[0:-1])
        if state == State.RIGHT:
            self.head.move_x_right()
        elif state == State.LEFT:
            self.head.move_x_left()
        elif state == State.UP:
            self.head.move_y_up()
        elif state == State.DOWN:
            self.head.move_y_down()
        self.snake[1:] = new_body

    def eat_itself(self):
        for i in range(1, self.snake_size):
            if self.head == self.snake[i]:
                return True
        return False

    def eat_food(self, food):
        return self.head == food
