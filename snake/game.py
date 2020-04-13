import random
import abc
from snake import Snake
from state import State
from point import Point
from screen import Screen
from characters import Characters


SPEED = 100

class Game(metaclass=abc.ABCMeta):

    def __init__(self, screen):
        self.screen = screen

    @abc.abstractmethod
    def play(self):
        pass


class GameSnake(Game):

    def __init__(self, screen, speed = 100):
        super(GameSnake, self).__init__(screen)
        # snake game variables
        init_pos_snake = [5, 5]
        init_snake_size = 4
        init_food_middle = True
        snake_head = Point(init_pos_snake[0], init_pos_snake[1])
        if init_food_middle:
            food = Point(screen.w//2, screen.h//2)
        self.player = Snake(snake_head, init_snake_size)
        self.goal = Point(random.randrange(1, screen.w-2), random.randrange(1, screen.h-2))
        self.state = State.RIGHT
        self.speed = speed
        self.score = 0
        self.max_score = 5
        self.winner_text = "WINNER! Final score: "
        self.game_over_text = "GAME OVER! Final score: "
        margin = 2
        final_head = Point(screen.w//2, screen.h//2 + margin)
        self.final_player = Snake(final_head, init_snake_size)
        self.final_goal = Point(final_head.x + len(self.game_over_text)-init_snake_size, final_head.y)
        self.final_text = Point(final_head.x - init_snake_size, final_head.y - margin)


    def print_player(self):
        self.screen.print_character(self.player.head, Characters.HEAD)
        for part in self.player.body:
            self.screen.print_character(part, Characters.BODY)

    def print_goal(self):
        self.screen.print_character(self.goal, Characters.SNAKE_GOAL)

    def print_game(self):
        self.screen.clear()
        self.print_player()
        self.print_goal()

    def print_end_game(self, text):
        self.screen.set_speed(-1)
        self.screen.clear()
        self.player = self.final_player
        self.goal = self.final_goal
        self.print_player()
        self.print_goal()
        self.screen.print_string(self.final_text, text)

    def play(self):
        self.screen.set_speed(self.speed)
        self.print_game()
        while True:
            if self.screen.is_outside_screen(self.player.head) or self.player.eat_itself():
                text = self.game_over_text + str(self.score)
                self.print_end_game(text)
                self.screen.close()
                return
            else:
                if self.player.eat_food(self.goal):
                    if self.score == self.max_score:
                        text = self.winner_text + str(self.score)
                        self.print_end_game(text)
                        self.screen.close()
                        return
                    else:
                        while True:
                            self.goal.change_point(random.randrange(1, self.screen.w-2), random.randrange(1, self.screen.h-2))
                            if self.goal != self.player.head:
                                break
                        self.score += 1
                        self.player.grow()
                self.state = self.screen.get_state(self.state)
                self.player.move(self.state)
                self.print_game()

if __name__ == "__main__":
    # create screen

    screen = Screen()
    screen.create()

    # create game

    game = GameSnake(screen, SPEED)
    game.play()
