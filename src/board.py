from _thread import start_new_thread
import numpy as np
import pygame
import math
from time import sleep


class Board():

    # board setiings
    POINT_DIST_FACT = 70
    SCREENSIZE = 1000
    EMPTY_RADIUS = 16
    POINT_RADIUS = 16
    BORDER_WIDTH = 3
    LINE_WIDTH = 2
    FONT = 'chalkduster.ttf'
    FONT_SIZE = 30

    # used color coding
    LIGHT_ORANGE = (255, 230, 205)
    ORANGE = (255, 223, 83)
    LIGHT_BLUE = (222, 222, 255)
    BLUE = (153, 153, 255)
    LIGHT_RED = (255, 222, 222)
    RED = (255, 153, 152)
    BLACK = (10, 10, 10)
    WHITE = (255, 255, 255)
    GRAY = (170, 170, 170)
    LIGHT_GREEN = (139, 230, 135)

    def __init__(self) -> None:
        """initilize the board by initializing the positions
        """
        self._init_state()
        pygame.init()
        self._screen = pygame.display.set_mode(
            [self.SCREENSIZE, self.SCREENSIZE])
        self._update()

    def _init_state(self) -> None:
        """Create a new board by positioning all pegs in there homes
        """
        """ the state has the following orm at the beginning:
        state = {-6: {-6 : -1, -5: -1,..., 6: -1},
                 -5: {-6 : -1, -5: -1,..., 6: -1},
                 -4: {-6 : -1, -5: -1,..., 6: -1},
                 ...,
                 4: {-6 : -1, -5: -1,..., 6: -1},
                 5: {-6 : -1, -5: -1,..., 6: -1},
                 6: {-6 : -1, -5: -1,..., 6: -1}
                }
        """
        state = {}
        for i in range(-7, 8):
            state[i] = {}
            for j in range(-7, 8):
                state[i][j] = -1

        # positions = np.zeros((13, 13))
        # positions[:][:] = -1
        state[-6][3] = 3  # player3 start

        state[-5][3] = 3  # player3 start
        state[-5][2] = 3  # player3 start

        state[-4][3] = 3  # player3 start
        state[-4][2] = 3  # player3 start
        state[-4][1] = 3  # player3 start

        state[-3][6] = 0
        state[-3][5] = 0
        state[-3][4] = 0
        state[-3][3] = 0
        state[-3][2] = 0
        state[-3][1] = 0
        state[-3][0] = 0
        state[-3][-1] = 0
        state[-3][-2] = 0
        state[-3][-3] = 0

        state[-2][5] = 0
        state[-2][4] = 0
        state[-2][3] = 0
        state[-2][2] = 0
        state[-2][1] = 0
        state[-2][0] = 0
        state[-2][-1] = 0
        state[-2][-2] = 0
        state[-2][-3] = 0

        state[-1][4] = 0
        state[-1][3] = 0
        state[-1][2] = 0
        state[-1][1] = 0
        state[-1][0] = 0
        state[-1][-1] = 0
        state[-1][-2] = 0
        state[-1][-3] = 0

        state[0][3] = 0
        state[0][2] = 0
        state[0][1] = 0
        state[0][0] = 0
        state[0][-1] = 0
        state[0][-2] = 0
        state[0][-3] = 0

        state[1][3] = 2  # player2 start
        state[1][2] = 0
        state[1][1] = 0
        state[1][0] = 0
        state[1][-1] = 0
        state[1][-2] = 0
        state[1][-3] = 0
        state[1][-4] = 1  # my start

        state[2][3] = 2  # player2 start
        state[2][2] = 2  # player2 start
        state[2][1] = 0
        state[2][0] = 0
        state[2][-1] = 0
        state[2][-2] = 0
        state[2][-3] = 0
        state[2][-4] = 1  # my start
        state[2][-5] = 1  # my start

        state[3][3] = 2  # player2 start
        state[3][2] = 2  # player2 start
        state[3][1] = 2  # player2 start
        state[3][0] = 0
        state[3][-1] = 0
        state[3][-2] = 0
        state[3][-3] = 0
        state[3][-4] = 1  # my start
        state[3][-5] = 1  # my start
        state[3][-6] = 1  # my start

        state[4][-1] = 0
        state[4][-2] = 0
        state[4][-3] = 0

        state[5][-2] = 0
        state[5][-3] = 0

        state[6][-3] = 0
        self.state = state

    def _update(self) -> None:
        """update the field by drawing the field and positions
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self._screen.fill((255, 255, 255))
        self._draw_field()
        self._draw_positions()
        pygame.display.flip()

    def _draw_field(self) -> None:
        """draw the playfield
        """
        # draw homes and dests
        my_home_points = [self._transformation(3, -6),
                          self._transformation(0, -3),
                          self._transformation(3, -3)]
        my_dest_points = [self._transformation(-3, 6),
                          self._transformation(0, 3),
                          self._transformation(-3, 3)]

        player2_home_points = [self._transformation(0, 3),
                               self._transformation(3, 0),
                               self._transformation(3, 3)]
        player2_dest_points = [self._transformation(-3, 0),
                               self._transformation(-3, -3),
                               self._transformation(0, -3)]

        player3_home_points = [self._transformation(-6, 3),
                               self._transformation(-3, 0),
                               self._transformation(-3, 3)]
        player3_dest_points = [self._transformation(6, -3),
                               self._transformation(3, -3),
                               self._transformation(3, 0)]

        pygame.draw.polygon(self._screen, self.LIGHT_ORANGE, my_home_points)
        pygame.draw.polygon(self._screen, self.LIGHT_ORANGE, my_dest_points)
        pygame.draw.polygon(self._screen, self.LIGHT_BLUE, player2_home_points)
        pygame.draw.polygon(self._screen, self.LIGHT_BLUE, player2_dest_points)
        pygame.draw.polygon(self._screen, self.LIGHT_RED, player3_home_points)
        pygame.draw.polygon(self._screen, self.LIGHT_RED, player3_dest_points)

        # draw lines in direction /
        for x in range(-6, 7):
            not_null = [k for k, v in self.state[x].items() if v != -1]
            y0 = min(not_null)
            y1 = max(not_null)
            x = x
            x0 = (x*-1) - y0
            x1 = (x*-1) - y1

            xt0, yt0 = self._transformation(x0, y0)
            xt1, yt1 = self._transformation(x1, y1)
            pygame.draw.line(self._screen, self.GRAY,
                             (xt0, yt0), (xt1, yt1), self.LINE_WIDTH)

            xt0, yt0 = self._transformation(x, y0)
            xt1, yt1 = self._transformation(x, y1)
            pygame.draw.line(self._screen, self.GRAY,
                             (xt0, yt0), (xt1, yt1), self.LINE_WIDTH)

        horizontal_line = [(-3, -2), (-3, -1), (-6, 3),
                           (-5, 3), (-4, 3), (-3, 3), (-3, 4), (-3, 5), (-3, 6), (1, 3), (2, 3)]

        for y, tupl in enumerate(horizontal_line):
            y = 5 - y
            xt0, yt0 = self._transformation(tupl[0], y)
            xt1, yt1 = self._transformation(tupl[1], y)
            pygame.draw.line(self._screen, self.GRAY,
                             (xt0, yt0), (xt1, yt1), self.LINE_WIDTH)

    def _draw_positions(self) -> None:
        """draw all positions
        """
        for x in range(-6, 7):
            for y in range(-6, 7):
                v = self.state[x][y]
                if v == 0:
                    x_koor, y_koor = self._transformation(
                        x, y)
                    pygame.draw.circle(self._screen, self.WHITE,
                                       (x_koor, y_koor), self.EMPTY_RADIUS)
                    pygame.draw.circle(self._screen, self.BLACK,
                                       (x_koor, y_koor), self.EMPTY_RADIUS, self.BORDER_WIDTH)
                elif v == 1:
                    x_koor, y_koor = self._transformation(
                        x, y)
                    pygame.draw.circle(self._screen, self.ORANGE,
                                       (x_koor, y_koor), self.POINT_RADIUS)
                    pygame.draw.circle(self._screen, self.BLACK,
                                       (x_koor, y_koor), self.POINT_RADIUS, self.BORDER_WIDTH)

                    font = pygame.font.SysFont(self.FONT, self.FONT_SIZE)
                    img = font.render('A', True, self.BLACK)
                    self._screen.blit(
                        img, (x_koor - self.FONT_SIZE/4, y_koor - self.FONT_SIZE/4))

                elif v == 2:
                    x_koor, y_koor = self._transformation(
                        x, y)
                    pygame.draw.circle(self._screen, self.BLUE,
                                       (x_koor, y_koor), self.POINT_RADIUS)
                    pygame.draw.circle(self._screen, self.BLACK,
                                       (x_koor, y_koor), self.POINT_RADIUS, self.BORDER_WIDTH)

                    font = pygame.font.SysFont(self.FONT, self.FONT_SIZE)
                    img = font.render('B', True, self.BLACK)
                    self._screen.blit(
                        img, (x_koor - self.FONT_SIZE/4, y_koor - self.FONT_SIZE/4))

                elif v == 3:
                    x_koor, y_koor = self._transformation(
                        x, y)
                    pygame.draw.circle(self._screen, self.RED,
                                       (x_koor, y_koor), self.POINT_RADIUS)
                    pygame.draw.circle(self._screen, self.BLACK,
                                       (x_koor, y_koor), self.POINT_RADIUS, self.BORDER_WIDTH)

                    font = pygame.font.SysFont(self.FONT, self.FONT_SIZE)
                    img = font.render('C', True, self.BLACK)
                    self._screen.blit(
                        img, (x_koor - self.FONT_SIZE/4, y_koor - self.FONT_SIZE/4))

    def _transformation(self, x: int, y: int) -> tuple:
        """Coordinate transformation

        Args:
            x (int): x koor before
            y (int): y koor before

        Returns:
            tuple: koor tuple after transformation
        """
        xt = (x + y * math.cos(math.pi / 3)) * self.POINT_DIST_FACT
        yt = (y * math.sin(math.pi / 3)) * self.POINT_DIST_FACT
        return self.SCREENSIZE/2 + xt, self.SCREENSIZE/2 - yt

    def change_state_w_pos(self, my_pegs: list, player2_pegs: list, player3_pegs: list) -> None:
        """Update the position of all pegs after the enemys moved the pegs

        Args:
            my_pegs (list): positions of all my pegs
            player2_pegs (list): positions of pegs of player 2
            player3_pegs ([type]): positions of pegs of player 3
        """
        for x in range(13):
            for y, v in enumerate(self.state):
                if v != -1:
                    self.state[x][y] = 0

        for x, y in my_pegs:
            self.state[x][y] = 1
            self._own_pegs_pos.append((x, y))

        for x, y in player2_pegs:
            self.state[x][y] = 2

        for x, y in player3_pegs:
            self.state[x][y] = 3
        self._update()

    def move_my_peg(self, peg_from: tuple, peg_to: tuple) -> None:
        """Move the peg from peg_from to peg_to 

        Args:
            peg_from (tuple): position to move peg from
            peg_to (tuple): position to move peg to
        """
        self.state[peg_from[0],
                   peg_from[1]] = 0
        self.state[peg_to[0], peg_to[1]] = 1
        self._own_pegs_pos.remove(peg_from)
        self._own_pegs_pos.append(peg_to)
        self._update()

    def set_state(self, state: dict) -> None:
        """set state of board and update field

        Args:
            state (dict): new state
        """
        self.state = state
        self._update()

    def mark_fields(self, marks: list) -> bool:
        """marks a list of positions if they are not already visited

        Args:
            marks (list): list of pos

        Returns:
            bool: all entrys were free
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self._screen.fill((255, 255, 255))
        self._draw_field()
        self._draw_positions()

        flag = True
        for x, y in marks:
            if self.state[x][y] != 0:
                flag = False
            x_koor, y_koor = self._transformation(
                x, y)
            pygame.draw.circle(self._screen, self.LIGHT_GREEN,
                               (x_koor, y_koor), self.EMPTY_RADIUS)
        pygame.display.flip()
        return flag
