from queue import Empty
import time
from math import sqrt
from min_queue import Queue
from algorithm_core import AlgorithmCore

COST = 1
DIAG_COST = sqrt(2)

class Jps:
    def __init__(self, data):
        self.map = data
        self.open_queue = Queue()
        self.close_list = {}
        self.path = []
        self.parent = {}
        self.cost = {}
        self.directions = [(1,1),(1,-1),(-1,1),(-1,-1), (1,0),(0,1),(0,-1),(-1,0)]
        self.ready = False

    def jps(self, start, end):
        time_start = time.time()
        jps = AlgorithmCore(self.map)
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
            self.expand_node(jps, node, end)
        print("Parent lista: ",self.parent)
        results = self.get_path(start, end)
        time_end = time.time()
        print("Aika:", time_end-time_start)
        return (self.parent, results)

    def expand_node(self, jps, node, end):
        for direction in self.directions:
            distance = self.cost[node[0]]
            if direction[0]+direction[1] == 0 or abs(direction[0]+direction[1])==2:
                scan = self.diag_scan(node, distance, direction, end)
            else:
                scan = self.hor_ver_scan(node, distance, direction, end)
            if not scan:
                if self.ready is True:
                    break
                continue
            if scan:
                g_value = scan[1]
                if scan[0] not in self.cost or g_value < self.cost[scan[0]]:
                    self.cost[scan[0]] = g_value
                    f_value = g_value + jps.euclidean(scan[0], end)
                    self.open_queue.add_to_queue((scan[0], f_value))
                    self.parent[scan[0]] = node[0]

    def hor_ver_scan(self, node, distance, direction, end):
        while True:
            next_x = node[0][0]+direction[0]
            next_y = node[0][1]+direction[1]
            if (next_x,next_y) == end:
                self.ready = True
                self.parent[(next_x, next_y)] = node[0]
                return ((next_x,next_y), 1)
            if self.map[next_x][next_y] == '.':
                dist = distance + COST
                next_x1 = next_x + direction[0]
                next_y1 = next_y + direction[1]
                if direction[1] == 0:
                    if self.map[next_x][next_y-1]!='.' and self.map[next_x1][next_y-1]=='.':
                        return ((next_x,next_y), dist, (direction[0], -1))
                    if self.map[next_x][next_y+1]!="." and self.map[next_x1][next_y+1]=='.':
                        return ((next_x,next_y), dist, (direction[0], -1))
                    return self.hor_ver_scan(((next_x,next_y),0), dist, direction, end)
                if direction[0] == 0:
                    if self.map[next_x-1][next_y]!='.' and self.map[next_x-1][next_y1]=='.':
                        return ((next_x,next_y), dist, (direction[0], -1))
                    if self.map[next_x+1][next_y]!="." and self.map[next_x+1][next_y1]=='.':
                        return ((next_x,next_y), dist, (direction[0], -1))
                    return self.hor_ver_scan(((next_x,next_y),0), dist, direction, end)
            return []
    
    def diag_scan(self, node, distance, direction, end):
        if direction[0]+direction[1] == 2:
            horizontal = (1,0)
            vertical = (0,1)
        elif direction[0]+direction[1] == -2:
            horizontal = (-1,0)
            vertical = (0,-1)
        elif direction == (-1,1):
            horizontal = (-1,0)
            vertical = (0,1)
        else:
            horizontal = (1,0)
            vertical = (0,-1)
        while True:
            next_x = node[0][0]+direction[0]
            next_y = node[0][1]+direction[1]
            if (next_x,next_y) == end:
                self.ready = True
                self.parent[(next_x, next_y)] = node[0]
                return ((next_x,next_y), 1)
            if self.map[next_x][next_y] == '.':
                dist = distance + DIAG_COST
                next_x1 = next_x + direction[0]
                next_y1 = next_y + direction[1]
                if self.map[node[0][0]][next_y]!='.' and self.map[node[0][0]][next_y1]=='.':
                    return ((next_x,next_y), dist, (-1*direction[0], direction[1]))
                if self.map[next_x][node[0][1]]!="." and self.map[next_x1][node[0][1]]=='.':
                    return ((next_x,next_y), dist, (direction[0], -1*direction[1]))
                hor_scan = self.hor_ver_scan(((next_x,next_y),0), dist, horizontal, end)
                if hor_scan:
                    return hor_scan
                ver_scan = self.hor_ver_scan(((next_x,next_y),0), dist, vertical, end)
                if ver_scan:
                    return ver_scan
                return self.diag_scan(((next_x,next_y),0), dist, direction, end)
            return []

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
