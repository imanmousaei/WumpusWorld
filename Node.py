"""
.: empty node
P: pit -> death
W: wumpus -> death
G: gold
"""

table = [
    ['.', '.', 'P', '.'],
    ['.', '.', '.', 'P'],
    ['P', 'W', '.', '.'],
    ['.', '.', 'P', 'G']
]

n = len(table)


class Node:
    def __init__(self, x=None, y=None, wumpus=False, pit=False, glitter=False, visited=False):
        self.x = x
        self.y = y
        self.wumpus = wumpus
        self.pit = pit
        self.glitter = glitter
        self.visited = visited

    def get_adj_nodes(self):
        return [nodes[self.x + 1][self.y], nodes[self.x - 1][self.y], nodes[self.x][self.y + 1],
                nodes[self.x][self.y - 1]]

    def safe(self):
        return not self.pit and not self.wumpus

    def stench(self):
        adj_nodes = self.get_adj_nodes()
        for node in adj_nodes:
            if node.wumpus:
                return True
        return False

    def breeze(self):
        adj_nodes = self.get_adj_nodes()
        for node in adj_nodes:
            if node.pit:
                return True
        return False


nodes = [[Node(x, y) for x in range(n + 1)] for y in range(n + 1)]


def config_nodes():
    for i in range(n):
        for j in range(n):
            if table[i][j] == 'W':
                nodes[i][j].wumpus = True
            elif table[i][j] == 'P':
                nodes[i][j].pit = True
            elif table[i][j] == 'G':
                nodes[i][j].glitter = True


