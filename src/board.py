from _thread import start_new_thread
import numpy as np
import pygame
import math
from time import sleep


class Board():

    # board setiings
    POINT_DIST_FACT = 70
    SCREENSIZE = 1000
    OFFSET = 6
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

    def __init__(self) -> None:
        """initilize the board by initializing the positions
        """
        self._init_positions()
        pygame.init()
        self._screen = pygame.display.set_mode(
            [self.SCREENSIZE, self.SCREENSIZE])
        self.update()

    def _init_positions(self):
        """Create a new board by positioning all pegs in there homes
        """
        positions = {}
        for i in range(-6, 7):
            positions[i] = {}
            for j in range(-6, 7):
                positions[i][j] = -1

        print(positions)
        positions = np.zeros((13, 13))
        positions[:][:] = -1
        positions[-6 + self.OFFSET][3 + self.OFFSET] = 3  # player3 start

        positions[-5 + self.OFFSET][3 + self.OFFSET] = 3  # player3 start
        positions[-5 + self.OFFSET][2 + self.OFFSET] = 3  # player3 start

        positions[-4 + self.OFFSET][3 + self.OFFSET] = 3  # player3 start
        positions[-4 + self.OFFSET][2 + self.OFFSET] = 3  # player3 start
        positions[-4 + self.OFFSET][1 + self.OFFSET] = 3  # player3 start

        positions[-3 + self.OFFSET][6 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][5 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][4 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][3 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][2 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][1 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][0 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][-1 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[-3 + self.OFFSET][-3 + self.OFFSET] = 0

        positions[-2 + self.OFFSET][5 + self.OFFSET] = 0
        positions[-2 + self.OFFSET][4 + self.OFFSET] = 0
        positions[-2 + self.OFFSET][3 + self.OFFSET] = 0
        positions[-2 + self.OFFSET][2 + self.OFFSET] = 0
        positions[-2 + self.OFFSET][1 + self.OFFSET] = 0
        positions[-2 + self.OFFSET][0 + self.OFFSET] = 0
        positions[-2 + self.OFFSET][-1 + self.OFFSET] = 0
        positions[-2 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[-2 + self.OFFSET][-3 + self.OFFSET] = 0

        positions[-1 + self.OFFSET][4 + self.OFFSET] = 0
        positions[-1 + self.OFFSET][3 + self.OFFSET] = 0
        positions[-1 + self.OFFSET][2 + self.OFFSET] = 0
        positions[-1 + self.OFFSET][1 + self.OFFSET] = 0
        positions[-1 + self.OFFSET][0 + self.OFFSET] = 0
        positions[-1 + self.OFFSET][-1 + self.OFFSET] = 0
        positions[-1 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[-1 + self.OFFSET][-3 + self.OFFSET] = 0

        positions[0 + self.OFFSET][3 + self.OFFSET] = 0
        positions[0 + self.OFFSET][2 + self.OFFSET] = 0
        positions[0 + self.OFFSET][1 + self.OFFSET] = 0
        positions[0 + self.OFFSET][0 + self.OFFSET] = 0
        positions[0 + self.OFFSET][-1 + self.OFFSET] = 0
        positions[0 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[0 + self.OFFSET][-3 + self.OFFSET] = 0

        positions[1 + self.OFFSET][3 + self.OFFSET] = 2  # player2 start
        positions[1 + self.OFFSET][2 + self.OFFSET] = 0
        positions[1 + self.OFFSET][1 + self.OFFSET] = 0
        positions[1 + self.OFFSET][0 + self.OFFSET] = 0
        positions[1 + self.OFFSET][-1 + self.OFFSET] = 0
        positions[1 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[1 + self.OFFSET][-3 + self.OFFSET] = 0
        positions[1 + self.OFFSET][-4 + self.OFFSET] = 1  # my start

        positions[2 + self.OFFSET][3 + self.OFFSET] = 2  # player2 start
        positions[2 + self.OFFSET][2 + self.OFFSET] = 2  # player2 start
        positions[2 + self.OFFSET][1 + self.OFFSET] = 0
        positions[2 + self.OFFSET][0 + self.OFFSET] = 0
        positions[2 + self.OFFSET][-1 + self.OFFSET] = 0
        positions[2 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[2 + self.OFFSET][-3 + self.OFFSET] = 0
        positions[2 + self.OFFSET][-4 + self.OFFSET] = 1  # my start
        positions[2 + self.OFFSET][-5 + self.OFFSET] = 1  # my start

        positions[3 + self.OFFSET][3 + self.OFFSET] = 2  # player2 start
        positions[3 + self.OFFSET][2 + self.OFFSET] = 2  # player2 start
        positions[3 + self.OFFSET][1 + self.OFFSET] = 2  # player2 start
        positions[3 + self.OFFSET][0 + self.OFFSET] = 0
        positions[3 + self.OFFSET][-1 + self.OFFSET] = 0
        positions[3 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[3 + self.OFFSET][-3 + self.OFFSET] = 0
        positions[3 + self.OFFSET][-4 + self.OFFSET] = 1  # my start
        positions[3 + self.OFFSET][-5 + self.OFFSET] = 1  # my start
        positions[3 + self.OFFSET][-6 + self.OFFSET] = 1  # my start

        positions[4 + self.OFFSET][-1 + self.OFFSET] = 0
        positions[4 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[4 + self.OFFSET][-3 + self.OFFSET] = 0

        positions[5 + self.OFFSET][-2 + self.OFFSET] = 0
        positions[5 + self.OFFSET][-3 + self.OFFSET] = 0

        positions[6 + self.OFFSET][-3 + self.OFFSET] = 0
        self._positions = positions

    def update(self):
        """update the field by drawing the field and positions
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self._screen.fill((255, 255, 255))
        self._draw_field()
        self._draw_positions()
        pygame.display.flip()

    def _draw_field(self):
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
        for x in range(1, 12):
            map_list = list(map(lambda x: x >= 0, self._positions[x]))
            y0 = map_list.index(1) - self.OFFSET
            y1 = len(self._positions[x]) - \
                map_list[::-1].index(1) - 1 - self.OFFSET
            x = x - self.OFFSET
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

    def _draw_positions(self):
        """draw all positions
        """
        for x in range(13):
            for y, v in enumerate(self._positions[x]):
                if v == 0:
                    x_koor, y_koor = self._transformation(
                        x - self.OFFSET, y - self.OFFSET)
                    pygame.draw.circle(self._screen, self.WHITE,
                                       (x_koor, y_koor), self.EMPTY_RADIUS)
                    pygame.draw.circle(self._screen, self.BLACK,
                                       (x_koor, y_koor), self.EMPTY_RADIUS, self.BORDER_WIDTH)
                elif v == 1:
                    x_koor, y_koor = self._transformation(
                        x - self.OFFSET, y - self.OFFSET)
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
                        x - self.OFFSET, y - self.OFFSET)
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
                        x - self.OFFSET, y - self.OFFSET)
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

    def change_pegs(self, my_pegs: list, player2_pegs: list, player3_pegs):
        """Update the position of all pegs after the enemys moved the pegs

        Args:
            my_pegs (list): positions of all my pegs
            player2_pegs (list): positions of pegs of player 2
            player3_pegs ([type]): positions of pegs of player 3
        """
        for x in range(13):
            for y, v in enumerate(self.positions):
                if v != -1:
                    self.positions[x][y] = 0

        for x, y in my_pegs:
            self.positions[x][y] = 1

        for x, y in player2_pegs:
            self.positions[x+self.OFFSET][y+self.OFFSET] = 2

        for x, y in player3_pegs:
            self.positions[x+self.OFFSET][y+self.OFFSET] = 3
        self.update()

    def move_peg(self, peg_from: tuple, peg_to: tuple):
        """Move the peg from peg_from to peg_to 

        Args:
            peg_from (tuple): position to move peg from
            peg_to (tuple): position to move peg to
        """
        self.positions[peg_from[0] + self.OFFSET,
                       peg_from[1] + self.OFFSET] = 0
        self.positions[peg_to[0] + self.OFFSET, peg_to[1] + self.OFFSET] = 1
        self.update()

    def get_all_pegs(self):
        pass

    def possible_moves(self, position: tuple) -> list:
        pass


Board()
sleep(10)
