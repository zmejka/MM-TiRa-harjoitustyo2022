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

    def jps(self, start, end):
        ''' JPS algoritmin päätoiminto:
        Args:
            start : alkuruutu
            end : kohderuutu
        '''
        time_start = time.time()    # aloitusaika
        jps = AlgorithmCore(self.map)
        self.end = end
        self.parent[start] = None       # alkuruudun ja alkuhinnan lisäykset listaan
        self.cost[start] = 0
        self.open_queue.add_to_queue((start, 0))    # alkusolu lusätty avoimeen listaan
        while not self.open_queue.is_empty():
            if self.ready is True:
                break
            node = self.open_queue.remove_from_queue()  # seuraava tarkastettava ruutu poistetaan listalta
            if node[0] == end:      # kohderuutu on löytynyt
                result_path = self.get_path(start, self.end)
                time_end = time.time()      # lopetusaika
                print("Aika:", time_end-time_start)
                return (self.parent, result_path)
            if node[0] in self.close_list:      # ruutu on jo tarkastettu
                continue
            self.close_list[node[0]] = self.cost[node[0]]
            self.expand_node(jps, node)     #kutsutaan laajennusmetodi
        time_end = time.time()
        print("Aika:", time_end-time_start)     # lasketaan kokonaisaika, joka on mennyt algoritmin toimintaan
        results = self.get_path(start, self.end)

        return (self.parent, results)

    def expand_node(self, jps, node):
        ''' Skannataan 8 suuntaa. '''
        for direction in DIRECTIONS:
            distance = self.cost[node[0]]
            if direction[0]+direction[1] == 0 or abs(direction[0]+direction[1])==2:     # diagonaaliset suunnat
                scan = self.diag_scan(node, distance, direction)
            else:
                scan = self.hor_ver_scan(node, distance, direction)         # horisontaalinen ja vertikaalinen suunta
            if not scan:
                continue
            if scan:
                if scan[0] == self.end:
                    self.parent[scan[0]] = node[0]
                    self.open_queue.add_to_queue((scan[0], 0))
                g_value = scan[1]
                if scan[0] not in self.cost or g_value < self.cost[scan[0]]:        # laskenta vastaa A* algoritmia
                    self.cost[scan[0]] = g_value
                    f_value = g_value + jps.euclidean(scan[0], self.end)
                    self.open_queue.add_to_queue((scan[0], f_value))
                    self.parent[scan[0]] = node[0]

    def hor_ver_scan(self, node, distance, direction):
        ''' Horisontaalinen ja vertikaalinen skannaus:
        Args:
            node : tarkistettava ruutu
            distance : etäisyys alkuruudusta tarkastettavaan ruutuun
            direction : koordinaattipari, joka määrä mihin suuntaan skannaus suoritetaan
        '''

        while True:
            next_x = node[0][0]+direction[0]
            next_y = node[0][1]+direction[1]
            if (next_x,next_y) == self.end:     # skannaus päätyy kohderuutuun
                self.ready = True
                self.parent[(next_x, next_y)] = node[0]
                return ((next_x,next_y), 1)
            if self.map[next_x][next_y] == '.':     # seuraava ruutu on avoin kulku
                dist = distance + COST
                next_x1 = next_x + direction[0]
                next_y1 = next_y + direction[1]
                if direction[1] == 0:           # horisontaalinen skannaus
                    if self.map[next_x][next_y-1]!='.' and self.map[next_x1][next_y-1]=='.':    # jump point
                        return ((next_x,next_y), dist, (direction[0], -1))
                    if self.map[next_x][next_y+1]!="." and self.map[next_x1][next_y+1]=='.':    # jump point
                        return ((next_x,next_y), dist, (direction[0], -1))
                    return self.hor_ver_scan(((next_x,next_y),0), dist, direction)      # skannausta jatketaan seuravaan ruutuun
                if direction[0] == 0:           # vertikaalinen skannaus
                    if self.map[next_x-1][next_y]!='.' and self.map[next_x-1][next_y1]=='.':    # jump point
                        return ((next_x,next_y), dist, (direction[0], -1))
                    if self.map[next_x+1][next_y]!="." and self.map[next_x+1][next_y1]=='.':    # jump point
                        return ((next_x,next_y), dist, (direction[0], -1))
                    return self.hor_ver_scan(((next_x,next_y),0), dist, direction)      # jatketaan skannausta
            return []
    
    def diag_scan(self, node, distance, direction):
        ''' Diagonaalinen skannaus:
        Args:
            node : tarkistettava ruutu
            distance : etäisyys alkuruudusta tarkastettavaan ruutuun
            direction : koordinaattipari, joka määrä mihin suuntaan skannaus suoritetaan
        '''

        if direction[0]+direction[1] == 2:      # poistetaan myöhemmin, määritetään skannaussuunnat
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
            if (next_x,next_y) == self.end:         # kohderuutu löytyi
                self.ready = True
                self.parent[(next_x, next_y)] = node[0]
                return ((next_x,next_y), 1)
            if self.map[next_x][next_y] == '.':     # kulku on mahdollinen
                dist = distance + DIAG_COST
                next_x1 = next_x + direction[0]
                next_y1 = next_y + direction[1]
                if self.map[node[0][0]][next_y]!='.' and self.map[node[0][0]][next_y1]=='.':    #jump point
                    return ((next_x,next_y), dist, (-1*direction[0], direction[1]))
                if self.map[next_x][node[0][1]]!="." and self.map[next_x1][node[0][1]]=='.':    #jump point
                    return ((next_x,next_y), dist, (direction[0], -1*direction[1]))
                hor_scan = self.hor_ver_scan(((next_x,next_y),0), dist, horizontal)     # skannataan horisontaalinen suunta
                if hor_scan:
                    return hor_scan
                ver_scan = self.hor_ver_scan(((next_x,next_y),0), dist, vertical)       # skannataan vertikaalinen suunta
                if ver_scan:
                    return ver_scan
                return self.diag_scan(((next_x,next_y),0), dist, direction)     # jatketaan diagonaaliskannausta
            return []

    def get_path(self, start, end):
        ''' Muodostetaan polku alkuruudusta loppuruutuun.
            Args:
                start : alkuruutu
                end : loppuruutu
        '''
        self.path.append(end)
        node = self.path[-1]
        while self.parent[node] is not None:
            if self.path[-1] == start:
                break
            self.path.append(self.parent.pop(self.path[-1]))
            node = self.path[-1]
        reversed_path = self.path[::-1]
        return reversed_path
