from board import Board
from algorithm import ChineseCheckerAlgorithm
from time import sleep


class ChineseCheckersMain():
    def __init__(self) -> None:
        self.board = Board()
        self.algo = ChineseCheckerAlgorithm()
        self._work()
        pass

    def _work(self):
        for st in self.algo.successor_states(self.board.state):
            self.board.set_state(st)

        pass


ChineseCheckersMain()
