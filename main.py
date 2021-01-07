from Node import Node, nodes, n, config_nodes


if __name__ == '__main__':
    config_nodes()
    print(nodes[1][1].get_adj_nodes())
