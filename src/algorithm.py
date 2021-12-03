from board import Board
import copy


class ChineseCheckerAlgorithm():
    def __init__(self) -> None:
        pass

    def _work(self):
        pass

    def successor_states(self, state: dict) -> list:
        """gets all the possible positions for a peg after all possible moves

        Returns:
            dict: dict with position of peg to move as key and all its successor states in a list as value
        """
        possible_moves = {}
        for x, y in self.get_own_pos(state):
            possible_moves[(x, y)] = []
            all_surrounding = [(x-1, y), (x+1, y), (x, y-1),
                               (x, y+1), (x-1, y-1), (x-1, y+1)]
            for x_m, y_m in all_surrounding:
                v = state[x_m][y_m]
                if v == 0:
                    possible_moves[(x, y)].append((x_m, y_m))
                elif v != -1:  # TODO: find all jumps possible
                    pass
        return self.possible_moves_to_states(state, possible_moves)

    def get_own_pos(self, state: dict) -> list:
        """gets all the pos of your pegs from state

        Args:
            state (dict): current state

        Returns:
            list: list of tuples with your pos
        """
        own_pos = []
        for x, inner_dict in state.items():
            own_pos += [(x, y) for y, v in inner_dict.items() if v == 1]
        return own_pos

    def possible_moves_to_states(self, state: dict, moves: dict) -> list:
        """turns a dict of possible moves in to list of states

        Args:
            state (dict): current state
            moves (dict): possible moves for all 6 pegs: moves = {(x_0, y_0): [(x_0_0, y_0_0), (x_0_1, y_0_1), ...],
                                                                  (x_1, y_1): [(x_1_0, y_1_0), (x_1_1, y_1_1), ...]
                                                                  ...}

        Returns:
            list: possible successor states
        """

        suc_states = []
        i = 0
        for (x0, y0), v in moves.items():
            for (x1, y1) in v:
                suc_states.append(copy.deepcopy(state))
                suc_states[i][x0][y0] = 0
                suc_states[i][x1][y1] = 1
                i += 1
        return suc_states

    def value_of_state(self, state: dict) -> int:
        """gets a state 

        Args:
            state (dict): possible state

        Returns:
            int: heuristic
        """
        pass

    def get_dist(posA: tuple, posB: tuple) -> int:
        way = 0
        xA, yA = posA
        xB, yB = posB
        # go left up first: \ untill x_B = x_A
