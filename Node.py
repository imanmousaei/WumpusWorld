from consts import table, n


class Node:
    def __init__(self, x=None, y=None, wumpus=False, pit=False, glitter=False, visited=False):
        self.x = x
        self.y = y
        self.wumpus = wumpus
        self.pit = pit
        self.glitter = glitter
        self.visited = visited

    def state(self):  # map every node to int, to use it as state id in Q-function
        return n * self.x + self.y

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


nodes = [[Node(x, y) for x in range(n)] for y in range(n)]


def config_nodes():
    for i in range(n):
        for j in range(n):
            if table[i][j] == 'W':
                nodes[i][j].wumpus = True
            elif table[i][j] == 'P':
                nodes[i][j].pit = True
            elif table[i][j] == 'G':
                nodes[i][j].glitter = True


