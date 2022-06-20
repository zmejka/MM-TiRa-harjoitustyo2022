''' A* - algorithm
    Args:
    DIRECTIONS : 8 suunnan siirtymäkoordinaatit
'''

import time
from min_queue import Queue
from algorithm_core import AlgorithmCore

DIRECTIONS = [(1,1),(1,-1),(1,0),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]

class AStar:
    ''' Args:
            map : karttadata matriisimuodossa
            open_queue : avoin-lista tarkistettavia ruutuja
            closed_list : lista ruutuja, jotka on jo tarkastettu
            parent : lista vanhempiruutuja polkun rakentamista varten
            cost : lista, johon on tallennettu etäisyydet alkuruudusta ruutuun
            ready : kohderuutu on loytynyt
            '''
    def __init__(self, data):
        self.map = data
        self.open_queue = Queue()
        self.close_list = {}
        self.parent = {}
        self.cost = {}
        self.ready = False
        self.a_star_core = AlgorithmCore(self.map)
        self.open_counter = 1
        self.close_counter = 0

    def a_star(self, start, end, heuristic, algorithm):
        ''' A* algoritmin päätoiminto:
        Args:
            start : alkuruutu
            end : kohderuutu
            heuristic : käytettävä heuristiikka
            algorithm : käytettävä algoritmi, A* tai Dijkstra
        '''
        time_start = time.time()
        self.parent[start] = None
        self.cost[start] = 0
        self.open_queue.add_to_queue((start, 0))
        while not self.open_queue.is_empty():
            if self.ready is True:
                break
            node = self.open_queue.remove_from_queue()
            if node[0] == end:
                result_path = self.a_star_core.get_path(end, self.parent)
                time_end = time.time()
                print("Aika:", round((time_end-time_start), 3))
                print("Lisätty avoimelle listalle: ", self.open_counter)
                print("Tarkistettu pisteittä: ", self.close_counter)
                return (self.parent, result_path)
            if node[0] in self.close_list:
                continue
            self.close_counter = self.close_counter + 1
            self.close_list[node[0]] = self.cost[node[0]]
            self.expand_node(node, end, heuristic, algorithm)
        time_end = time.time()
        print("Aika:", round((time_end-time_start), 3))
        print("Lisätty avoimelle listalle: ", self.open_counter)
        print("Tarkistettu pisteittä: ", self.close_counter)
        if self.ready:
            results = self.a_star_core.get_path(end, self.parent)
            return (self.parent, results)
        return "Polkua ei löytynyt!"

    def expand_node(self, node, end, heuristic, algorithm):
        ''' Skannataan 8 suuntaa.
        Args:
            a_star : algoritmi
            node : tarkastettava ruutu
            end : kohderuutu
            algorithm : käytettävä algoritmi (A* tai Dijkstra)
            heuristic : käytettävä heiristiikka
        '''

        for direction in DIRECTIONS:
            position = (node[0][0]+direction[0], node[0][1]+direction[1])
            if position == end:
                self.parent[position] = node[0]
                self.ready = True
                break
            if self.map[position[0]][position[1]] == '.':
                g_value = self.cost[node[0]] + self.a_star_core.heuristic_method(node[0], position, heuristic)
                if position not in self.cost or g_value < self.cost[position]:
                    self.cost[position] = g_value
                    if algorithm == 1:
                        f_value = g_value + self.a_star_core.heuristic_method(position, end, heuristic)
                        self.open_counter = self.open_counter + 1
                        self.open_queue.add_to_queue((position, f_value))
                        self.parent[position] = node[0]
                    else:
                        self.open_counter = self.open_counter + 1
                        self.open_queue.add_to_queue((position, g_value))
                        self.parent[position] = node[0]
