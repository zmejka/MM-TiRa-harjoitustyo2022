import time
from min_queue import Queue
from algorithm_core import AlgorithmCore

class AStar:
    def __init__(self, data):
        self.map = data
        self.open_queue = Queue()
        self.close_list = {}
        self.path = []
        self.parent = {}
        self.cost = {}
        self.directions = [(1,1),(1,-1),(1,0),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
        self.ready = False

    def a_star(self, start, end):
        time_start = time.time()
        a_star = AlgorithmCore(self.map)
        self.parent[start] = None
        self.cost[start] = 0
        self.open_queue.add_to_queue((start, 0))
        while not self.open_queue.is_empty():
            if self.ready is True:
                break
            node = self.open_queue.remove_from_queue()
            if node[0] == end:
                result_path = self.get_path(start, end)
                time_end = time.time()
                print("Aika:", time_end-time_start)
                return (self.parent, result_path)
            if node[0] in self.close_list:
                continue
            self.close_list[node[0]] = self.cost[node[0]]
            self.expand_node(a_star, node, end)
        print("Vanhempi lista: ", self.parent)
        results = self.get_path(start, end)
        time_end = time.time()
        print("Aika:", time_end-time_start)
        return (self.parent, results)

    def expand_node(self, a_star, node, end):
        for direction in self.directions:
            position = (node[0][0]+direction[0], node[0][1]+direction[1])
            if position == end:
                self.parent[position] = node[0]
                self.ready = True
                break
            if self.map[position[0]][position[1]] == '.':
                g_value = self.cost[node[0]] + a_star.euclidean(node[0], position)
                if position not in self.cost or g_value < self.cost[position]:
                    self.cost[position] = g_value
                    f_value = g_value + a_star.euclidean(position, end)
                    self.open_queue.add_to_queue((position, f_value))
                    self.parent[position] = node[0]

    def get_path(self, start, end):
        self.path.append(end)
        node = self.path[-1]
        while self.parent[node] is not None:
            if self.path[-1] == start:
                break
            self.path.append(self.parent.pop(self.path[-1]))
            node = self.path[-1]
        reversed_path = self.path[::-1]
        return reversed_path
