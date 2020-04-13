import curses
import time
from state import State
from characters import Characters

class Screen:
    def __init__(self):
        self.stdsrc = curses.initscr()
        self._h, self._w = self.stdsrc.getmaxyx()

    @property
    def h(self):
        return self._h

    @property
    def w(self):
        return self._w

    def create(self):
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        self.stdsrc.keypad(True)
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def close(self):
        self.stdsrc.getch()
        time.sleep(1)
        # reverse terminal settings
        curses.nocbreak()
        self.stdsrc.keypad(False)
        curses.echo()

        # close the application
        curses.endwin()

    def set_speed(self, speed):
        self.stdsrc.timeout(speed)

    def is_outside_screen(self, player):
        return player.x == self.w-1 or player.x == 0 or player.y == 0 or player.y == self.h-1

    def print_character(self, element, character):
        if character == Characters.SNAKE_GOAL:
           self.stdsrc.addch(element.y, element.x, curses.ACS_DIAMOND)
        elif character == Characters.HEAD:
            self.stdsrc.attron(curses.color_pair(1))
            self.stdsrc.addch(element.y, element.x, ' ')
            self.stdsrc.attroff(curses.color_pair(1))
        elif character == Characters.BODY:
            self.stdsrc.addch(element.y, element.x, curses.ACS_BLOCK)
        self.stdsrc.refresh()

    def print_string(self, element, text):
        self.stdsrc.addstr(element.y, element.x, text)
        self.stdsrc.refresh()

    def clear(self):
        self.stdsrc.clear()

    def get_state(self, state):
        key = self.stdsrc.getch()
        new_state = state
        if key == curses.KEY_UP and state != State.DOWN:
            new_state = State.UP
        elif key == curses.KEY_DOWN and state != State.UP:
            new_state = State.DOWN
        elif key == curses.KEY_LEFT and state != State.RIGHT:
            new_state = State.LEFT
        elif key == curses.KEY_RIGHT and state != State.LEFT:
            new_state = State.RIGHT
        return new_state

