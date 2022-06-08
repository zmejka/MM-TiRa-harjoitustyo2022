''' JPS - algorithm
    Args:
    COST : verekkäin olevien ruutujen hinta, 1
    DIAG_COST : diagonaalisesti vierekkäin olevien ruutujen hinta, neliöjuuri 2
    DIRECTIONS : 8 suunnan siirtymäkoordinaatit
'''
import time
from math import sqrt

from min_queue import Queue
from algorithm_core import AlgorithmCore

COST = 1
DIAG_COST = sqrt(2)
DIRECTIONS = [(1,1),(1,-1),(-1,1),(-1,-1), (1,0),(0,1),(0,-1),(-1,0)]

class Jps:
    ''' Args:
            map : karttadata matriisimuodossa
            open_queue : avoin-lista tarkistettavia ruutuja
            clesed_list : lista ruutuja, jotka on jo tarkastettu
            path : polku alkuruudusta kohderuutuun
            parent : lista vanhempiruutuja polkun rakentamista varten
            cost : lista, johon on tallennettu etäisyydet alkuruudusta ruutuun
            ready : kohderuutu on loytynyt
            end : kohderuutu
            '''
    def __init__(self, data):
        self.map = data
        self.open_queue = Queue()
        self.close_list = {}
        self.path = []
        self.parent = {}
        self.cost = {}
        self.ready = False
        self.end = (0,0)
        self.jps_core = AlgorithmCore(self.map)

    def jps(self, start, end):
        ''' JPS algoritmin päätoiminto:
        Args:
            start : alkuruutu
            end : kohderuutu
        '''
        time_start = time.time()    # aloitusaika
        self.end = end
        self.parent[start] = None       # alkuruudun ja alkuhinnan lisäykset listaan
        self.cost[start] = 0
        self.open_queue.add_to_queue((start, 0))    # alkusolu lusätty avoimeen listaan
        print("Koordinaatit: ", start, end)

        while not self.open_queue.is_empty():
            if self.ready:
                break
            node = self.open_queue.remove_from_queue()  # seuraava tarkastettava ruutu poistetaan listalta
            print(node)
            if node[0] == end:      # kohderuutu on löytynyt
                result_path = self.jps.get_path(start, self.end, self.parent)
                time_end = time.time()      # lopetusaika
                print("Aika:", time_end-time_start)
                return (self.parent, result_path)
            if node[0] in self.close_list:      # ruutu on jo tarkastettu
                continue
            self.close_list[node[0]] = self.cost[node[0]]
            self.expand_node(node)     #kutsutaan laajennusmetodi
        time_end = time.time()
        print("Aika:", time_end-time_start)     # lasketaan kokonaisaika, joka on mennyt algoritmin toimintaan
        print(self.open_queue.get_queue(), self.ready)
        results = self.jps_core.get_path(start, self.end, self.parent)

        return (self.parent, results)

    def expand_node(self, node):
        ''' Skannataan 8 suuntaa. '''
        for direction in DIRECTIONS:
            distance = self.cost[node[0]]
            scan = self.jump(node, distance, direction)
            print("Palautettu:", scan)
            if scan is None or scan in self.close_list:
                continue

            if self.ready:
                self.parent[self.end] = node[0]
                self.new_jump_point((scan[0], 1), node)

            self.new_jump_point(scan, node)
    
    def new_jump_point(self, node, parent_node):
        g_value = node[1]
        if node[0] not in self.cost or g_value < self.cost[node[0]]:        # laskenta vastaa A* algoritmia
            self.cost[node[0]] = g_value
            f_value = g_value + self.jps_core.euclidean(node[0], self.end)
            self.open_queue.add_to_queue((node[0], f_value))
            self.parent[node[0]] = parent_node[0]

    def jump(self, node, distance, direc):
        ''' Horisontaalinen ja vertikaalinen skannaus:
        Args:
            node : tarkistettava ruutu
            distance : etäisyys alkuruudusta tarkastettavaan ruutuun
            direction : koordinaattipari, joka määrä mihin suuntaan skannaus suoritetaan
        '''
        next_x = node[0][0]+direc[0]
        next_y = node[0][1]+direc[1]
        dist = distance + COST
        if self.map[next_x][next_y] != '.':
            return None
        if (next_x,next_y) == self.end:     # skannaus päätyy kohderuutuun
            print("loppusolu")
            self.ready = True
            return (next_x,next_y), dist
        if self.map[next_x][next_y] == '.':     # seuraava ruutu on avoin kulku
            if direc[0] != 0 and direc[1] != 0:     # diagonal scan
                dist = distance + DIAG_COST
                if self.map[next_x-direc[0]][next_y]!='.' and self.map[next_x-direc[0]][next_y+direc[1]]=='.' or \
                    self.map[next_x][next_y-direc[1]]!='.' and self.map[next_x+direc[0]][next_y-direc[1]]=='.' or \
                    self.map[next_x][next_y+direc[1]]!='.' and self.map[next_x+direc[0]][next_y]=='.':
                    return (next_x,next_y),dist
                if self.jump(((next_x+direc[0],next_y),0), dist, (direc[0],0)) != None or \
                    self.jump(((next_x,next_y+direc[1]),0), dist, (0, direc[1])) != None:
                    return (next_x,next_y),dist
            else:
                if direc[1] == 0:           # horisontaalinen skannaus
                    if self.map[next_x][next_y-1]!='.' and self.map[next_x+direc[0]][next_y-1]=='.' or \
                        self.map[next_x][next_y+1]!='.' and self.map[next_x+direc[0]][next_y+1]=='.':    # jump point
                        return (next_x,next_y),dist
                if direc[0] == 0:           # vertikaalinen skannaus
                    if self.map[next_x-1][next_y]!='.' and self.map[next_x-1][next_y+direc[1]]=='.' or \
                        self.map[next_x+1][next_y]!='.' and self.map[next_x+1][next_y+direc[1]]=='.':    # jump point
                        return (next_x,next_y),dist
        return self.jump(((next_x,next_y),0), dist, direc)
    
    def direction_choise(self, direction):
        if direction[0]+direction[1] == 2:
            return [(1,0),(0,1)]
        elif direction[0]+direction[1] == -2:
            return [(-1,0),(0,-1)]
        elif direction == (-1,1):
            return [(-1,0), (0,1)]
        else:
            return [(1,0), (0,-1)]
