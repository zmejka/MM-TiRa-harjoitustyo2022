''' A* - algorithm
    Args:
    DIRECTIONS : 8 suunnan siirtymäkoordinaatit
'''

from min_queue import Queue
from algorithm_core import AlgorithmCore

DIRECTIONS = [(1,1),(1,-1),(1,0),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]

class AStar:
    ''' Args:
            map : karttadata matriisimuodossa
            open_queue : avoin minimikeko, tarkastusjonossa olevia ruutuja
            close_list : lista ruutuja, jotka ovat jo tarkastettu
            parent : lista vanhempiruutuja polun rakentamista varten
            cost : lista, johon on tallennettu etäisyydet alkuruudusta ruutuun
            ready : True, jos kohderuutu on loytynyt, False muulloin
            a_star_core : algoritmin perustominnot
            open_counter : laskee avoimelle listalle lisätyt ruudut
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

    def a_star(self, start, end, heuristic, algorithm):
        ''' A* algoritmin päätoiminto:
        Args:
            start : alkuruutu
            end : kohderuutu
            heuristic : käytettävä heuristiikka
            algorithm : käytettävä algoritmi, A* tai Dijkstra

        Alkuruutu lisätään avoimelle listalle, parent listalle sekä cost-listalle.
            Alkuruudun hinta on 0.
        Niin kauan, että minimikeossa on ruutuja:
            Tarkistetaan, onko kohderuutu on lyötynyt.
                Jos ei, poimitaan ruutu keosta.
            Jos poimittu ruutu on kohderuutu, kutsutaan polun muodostus metodi ja
                palautetaan tulokset.
            Jos poimittu ruutu on close-listalla, jatketaan seuraavaan ruutuun
            Muuten kutsutaan laajennusmetodi.
        Jos minimikeossa ei ole enää ruutuja tai kohderuutu on löytynyt,
            Kutsutaan polun muodostus metodia tai palautetaan tiedon, että polkua ei löytynyt.

        Returns:
            Jos ei polkua palautetaan:
                String : "Polkua ei löytynyt"
            Muulloin palautetaan:
                Tuple : parent-lista, polku, minimikeon laskurin arvo, close-lista
        '''
        self.parent[start] = None
        self.cost[start] = 0
        self.open_queue.add_to_queue((start, 0))
        while not self.open_queue.is_empty():
            if self.ready is True:
                break
            node = self.open_queue.remove_from_queue()
            if node[0] == end:
                result_path = self.a_star_core.get_path(end, self.parent)
                return (self.parent, result_path, self.open_counter, len(self.close_list))
            if node[0] in self.close_list:
                continue
            self.close_list[node[0]] = self.cost[node[0]]
            self.expand_node(node, end, heuristic, algorithm)
        if self.ready:
            results = self.a_star_core.get_path(end, self.parent)
            return (self.parent, results[0], self.open_counter, len(self.close_list), results[1])
        return "Polkua ei löytynyt!"

    def expand_node(self, node, end, heuristic, algorithm):
        ''' Ruudun skannaus 8 suuntaan.
        Args:
            node : tarkastettava ruutu
            end : kohderuutu
            algorithm : käytettävä algoritmi (A* tai Dijkstra)
            heuristic : käytettävä heiristiikka

        Jokaiseen annetun suuntaan: lasketaan naapuriruudun koordinaatit.
        Jos naapuriruutu on kohderuutu:
            listätään annettu ruutu parent listaan ja
                asetetaan ready-arvo True:ksi
        Muulloin:
            jos naapuriruutu ei ole kartalla,
                jatketaan seuraavaan suuntaan
            jos naapuriruutu ei ole este, lasketaan g-arvo
                (etäisyys alkuruudusta tarkistettavaan ruutuun)
            jos käytössä Dijkstra algoritmi:
                lisätään minimikekon laskuriin 1 ja lisätään kekoon tuple : koordinaatit, g-arvo
                lisätään parent listaan tarkastettavan ruudun vanhemmaksi annettu ruutu
            jos käytössä A* algoritmi:
                lasketaan f-arvo (heuristinen etäisyys ruudusta kohderuutuun)
                lisätään minimikekon laskuriin 1 ja lisätään kekoon tuple : koordinaatit, f-arvo
                lisätään parent listaan tarkastettavan ruudun vanhemmaksi annettu ruutu
        '''

        for direction in DIRECTIONS:
            position = (node[0][0]+direction[0], node[0][1]+direction[1])
            if position[0] > len(self.map)-1 or position[0] < 1:
                continue
            if position[1] > len(self.map[0])-1 or position[1] < 1:
                continue
            if position == end:
                self.parent[position] = node[0]
                self.ready = True
                break
            if self.map[position[0]][position[1]] == '.':
                g_value = self.cost[node[0]] + self.a_star_core.heuristic_method(node[0], \
                    position, heuristic)
                if position not in self.cost or g_value < self.cost[position]:
                    self.cost[position] = g_value
                    if algorithm == 1:
                        f_value = g_value + self.a_star_core.heuristic_method(position, \
                            end, heuristic)
                        self.open_counter = self.open_counter + 1
                        self.open_queue.add_to_queue((position, f_value))
                        self.parent[position] = node[0]
                    else:
                        self.open_counter = self.open_counter + 1
                        self.open_queue.add_to_queue((position, g_value))
                        self.parent[position] = node[0]
