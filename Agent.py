from Node import nodes, n
from consts import *


class Agent:
    def __init__(self, current_node=nodes[0][0]):
        self.current_node = current_node

    def respawn(self):
        state = self.current_node.state()
        self.current_node = nodes[0][0]
        return state

    def state(self):
        return self.current_node.state()

    def move(self, action):
        """
        :param action:
            0 : Up
            1 : Right
            2 : Down
            3 : Left
        :return: (ended, reward)
            ended: True iff the game is ended(die or grab Gold)
            reward: score given for only this action
        """
        if action == 0:
            self.current_node = nodes[self.current_node.x][min(self.current_node.y+1, n-1)]
        elif action == 1:
            self.current_node = nodes[min(self.current_node.x+1, n-1)][self.current_node.y]
        elif action == 2:
            self.current_node = nodes[max(self.current_node.x-1, 0)][self.current_node.y]
        elif action == 3:
            self.current_node = nodes[self.current_node.x][max(self.current_node.y-1, 0)]

        if self.current_node.wumpus or self.current_node.pit:
            return True, DIE_REWARD
        elif self.current_node.glitter:
            return True, WIN_REWARD
        else:
            return False, ELSE_REWARD
