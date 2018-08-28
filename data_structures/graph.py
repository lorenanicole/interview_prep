from collections import defaultdict


class Graph(object):
    """
    Ref: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
    """
    def __init__(self, nodes):
        self.nodes_to_edges = defaultdict(list, **nodes) if nodes else defaultdict(list)

    def add_edge(self, start_node, end_node):
        self.nodes_to_edges[start_node].append(end_node)

    def add_node(self, node):
        self.nodes_to_edges[node] = None

    def find_path(self, start_node, end_node):
        """
        :param start_node: node to start from
        :param end_node: node to end at

        :return a str including all nodes crossed along the path, if no complete path
        return the partial path
        """
        pass

    def generate_edges(self):
        pass

    def find_all_paths(self, start_node, end_node):
        pass

    def find_shortest_path(self, start_node, end_node, path):
        pass