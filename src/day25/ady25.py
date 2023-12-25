from networkx import minimum_edge_cut, connected_components, Graph

input = 'input/day25'

def partOne():
    g = Graph()

    for line in open(input).read().splitlines():
        left, right = line.split(":")
        for node in right.strip().split():
            g.add_edge(left, node)
            g.add_edge(node, left)

    g.remove_edges_from(minimum_edge_cut(g))
    a, b = connected_components(g)

    print(len(a) * len(b))

x
partOne()