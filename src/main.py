from board import Board
from algorithm import ChineseCheckerAlgorithm
from time import sleep


class ChineseCheckersMain():
    def __init__(self) -> None:
        self.board = Board()
        self._work()
        pass

    def _work(self):
        sleep(5)
        current_pos = (3, -4)
        self.board.move_pug(current_pos, (2, -3))
        sleep(3)
        pass


ChineseCheckersMain()
